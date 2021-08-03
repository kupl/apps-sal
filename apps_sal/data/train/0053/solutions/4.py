def makeRepeat(s):
    repeat = [[s[0], 0]]
    for ch in s:
        if ch == repeat[-1][0]:
            repeat[-1][1] += 1
        else:
            repeat.append([ch, 1])
    return repeat


def solve(N, S):
    assert len(S) == N - 1
    curr = 0
    repeat = makeRepeat(S)
    longest = list(range(1, N + 1))
    shortest = list(reversed(list(range(1, N + 1))))
    for ch, count in repeat:
        if ch == ">":
            longest[curr: curr + count + 1] = reversed(
                longest[curr: curr + count + 1]
            )
        else:
            assert ch == "<"
            shortest[curr: curr + count + 1] = reversed(
                shortest[curr: curr + count + 1]
            )
        curr += count

    # print(" " + " ".join(S))
    return " ".join(map(str, shortest)) + "\n" + " ".join(map(str, longest))


def __starting_point():
    T, = list(map(int, input().split()))
    for t in range(T):
        N, S = input().split()
        N = int(N)
        ans = solve(N, S)
        print(ans)


__starting_point()
