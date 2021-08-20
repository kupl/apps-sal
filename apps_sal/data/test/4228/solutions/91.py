(N, L) = map(int, input().split())
s = N * (2 * L + N - 1) // 2
l = [abs(L + i) for i in range(N)]
print(s - (L + l.index(min(l))))
