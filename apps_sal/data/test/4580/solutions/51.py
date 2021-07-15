n = int(input())
A = list(map(int, input().split()))

rate = [0 for _ in range(9)]

for a in A:
    if a < 400:
        rate[0] += 1
    elif a < 800:
        rate[1] += 1
    elif a < 1200:
        rate[2] += 1
    elif a < 1600:
        rate[3] += 1
    elif a < 2000:
        rate[4] += 1
    elif a < 2400:
        rate[5] += 1
    elif a < 2800:
        rate[6] += 1
    elif a < 3200:
        rate[7] += 1
    else:
        rate[8] += 1

ans = 0
for i in range(8):
    if rate[i] >= 1:
        ans += 1
if ans == 0:
    print(1, rate[8])
else:
    print(ans, ans + rate[8])
