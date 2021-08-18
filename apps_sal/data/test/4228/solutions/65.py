N, L = map(int, input().split())

s = N * (2 * L + N - 1) // 2
if L + N - 1 < 0:
    eat = L + N - 1
elif L > 0:
    eat = L
else:
    eat = 0

print(s - eat)
