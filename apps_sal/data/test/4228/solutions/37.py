(N, L) = map(int, input().split())
s = (L * 2 + N - 1) * N // 2
if L >= 0:
    print(s - L)
elif L + N - 1 <= 0:
    print(s - L - N + 1)
else:
    print(s)
