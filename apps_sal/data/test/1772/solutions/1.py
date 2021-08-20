n = int(input())
f = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
for i in range(n):
    if f[i] % 2 != 0:
        cnt1 += 1
    else:
        cnt2 += 1
if cnt1 <= cnt2:
    print(cnt1)
else:
    print(cnt2 + (cnt1 - cnt2) // 3)
