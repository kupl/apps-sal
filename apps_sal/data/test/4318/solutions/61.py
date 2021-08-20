n = int(input())
h = list(map(int, input().split()))
cnt = 1
wk = h[0]
for i in range(n - 1):
    if wk <= h[i + 1]:
        cnt += 1
        wk = h[i + 1]
print(cnt)
