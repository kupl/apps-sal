from collections import Counter

N = int(input())
abs_diffs = list(map(int, input().split()))

if N % 2 == 0:
    expected = [i // 2 * 2 + 1 for i in range(N)]
    dims = N // 2
else:
    expected = [(i + 1) // 2 * 2 for i in range(N)]
    dims = (N - 1) // 2

if sorted(abs_diffs) == expected:
    print((2 ** dims % (10 ** 9 + 7)))

else:
    print((0))
