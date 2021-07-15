def main():
    from bisect import bisect
    from itertools import accumulate, chain
    from sys import stdin, stdout

    input = stdin.readline
    input()
    s = sorted(set(map(int, input().split())))
    n = len(s)
    inp = sorted((a - b for (a, b) in zip(s[1:], s)))
    acc = tuple(chain(accumulate(inp), (0,)))
    for _ in range(int(input())):
        l_, r = list(map(int, input().split()))
        d = r + 1 - l_
        i = bisect(inp, d)
        stdout.write(f'{acc[i - 1] + (n - i) * d} ')


main()

