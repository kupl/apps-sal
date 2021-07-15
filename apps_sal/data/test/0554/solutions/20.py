n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
brr = [list(map(int, input().split())) for i in range(m)]
pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + arr[i]
cnt = 0
for i in range(m):
    cnt += 0 if pref[brr[i][1]]- pref[brr[i][0] - 1] < 0 else pref[brr[i][1]]- pref[brr[i][0] - 1]
print(cnt)
