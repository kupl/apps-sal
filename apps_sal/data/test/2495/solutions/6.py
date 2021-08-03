from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

a = list(accumulate(a))

ans1 = 0
tmp1 = 0
for i in range(n):
    b = a[i] + tmp1
    if i % 2 == 0 and b <= 0:
        tmp1 += 1 - b
        ans1 += 1 - b
    elif i % 2 == 1 and b >= 0:
        tmp1 += -1 - b
        ans1 += 1 + b

ans2 = 0
tmp2 = 0
for i in range(n):
    b = a[i] + tmp2
    if i % 2 == 1 and b <= 0:
        tmp2 += 1 - b
        ans2 += 1 - b
    elif i % 2 == 0 and b >= 0:
        tmp2 += -1 - b
        ans2 += 1 + b

ans = min(ans1, ans2)
print(ans)
