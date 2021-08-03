(n, d) = list(map(int, input().split()))
songs = list(map(int, input().split()))

time_used = sum(songs) + (n - 1) * 10
if (time_used > d):
    print(-1)
else:
    print((d - time_used) // 5 + 2 * (n - 1))
