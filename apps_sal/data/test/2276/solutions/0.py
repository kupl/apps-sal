
memo = {}


def f(dat, rewards, start, end, extra):
    curr = (start, end, extra)
    if curr in memo:
        return memo[curr]

    if start > end:
        return 0
    if start == end:
        memo[curr] = rewards[dat[start] + extra]
        return memo[curr]

    out = 0
    for cut in range(end, start - 1, -2):
        if cut == end:
            out_curr = rewards[dat[cut] + extra]
            out_curr += f(dat, rewards, start, cut - 1, 0)
        else:
            out_curr = f(dat, rewards, start, cut, extra + dat[end])
            out_curr += f(dat, rewards, cut + 1, end - 1, 0)

        out = max(out, out_curr)

    memo[curr] = out
    return memo[curr]


def solve(dat_str, rewards_orig):
    dat = []
    pos = 0
    while pos < len(dat_str):
        end = pos
        while end < len(dat_str) and dat_str[pos] == dat_str[end]:
            end += 1

        dat.append(end - pos)
        pos = end

    rewards = [0, rewards_orig[0]]
    for k in range(2, len(rewards_orig) + 1):
        rewards.append(
            max(
                rewards[k - j] + rewards_orig[j - 1]
                for j in range(1, k + 1)
            )
        )

    return f(dat, rewards, 0, len(dat) - 1, 0)


int_dummy = input()
dat_str = input().strip()
rewards_input = input().strip().split()
rewards_ints = [int(x) for x in rewards_input]


print((
    solve(
        dat_str,
        rewards_ints,
    )
))
