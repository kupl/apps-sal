n = int(input())
s = list(map(int, input().split()))
k = 0
m = 0
for i in range(len(s)):
    if s[i] == 0:
        k += 1
    else:
        m += 1
if k == 0:
    print(-1)
elif m < 9:
    print(0)
else:
    x = m // 9
    print('5' * 9 * x + '0' * k)

