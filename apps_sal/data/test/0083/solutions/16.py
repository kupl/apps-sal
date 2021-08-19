n = int(input())
a = list(map(int, input().split()))
p = 0
flag = True
m = 0
for i in range(len(a)):
    if a[i] < 0:
        m += 1
    if a[i] > 0:
        p += 1
if m > p:
    if n // 2 + n % 2 <= m:
        print(-1)
        flag = False
elif n // 2 + n % 2 <= p:
    print(1)
    flag = False
if flag:
    print(0)
