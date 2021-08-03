n = int(input())
s = list(input())
abc = 'abcdefghijklmnopqrstuvwxyz'
limit = list(map(int, input().split()))
mod = int(1e9) + 7
memo = [None] * n


def main():
    num_ways, longest, min_num = split(0)
    print(num_ways)
    print(longest)
    print(min_num)


def split(start):
    if start >= len(s):
        return 1, 0, 0

    if memo[start] is not None:
        return memo[start]

    num_ways = 0
    longest = 0
    min_num = 1e5

    max_allowed = 1e5

    for i in range(start, len(s)):
        current_length = i - start + 1
        max_allowed = min(max_allowed, limit[abc.find(s[i])])
        if current_length > max_allowed:
            break

        longest = max(current_length, longest)
        ss_num_ways, ss_longest, ss_min_num = split(i + 1)
        num_ways = (num_ways + ss_num_ways) % mod
        longest = max(longest, ss_longest)
        min_num = min(min_num, ss_min_num + 1)

    memo[start] = num_ways, longest, min_num
    return memo[start]


def __starting_point():
    main()


__starting_point()
