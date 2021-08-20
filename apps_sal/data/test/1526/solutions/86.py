N = list(map(int, input().split()))
N.sort()
cnt = 0
cnt += N[2] - N[1]
(x, y) = divmod(N[1] - N[0], 2)
cnt += x + y * 2
print(cnt)
