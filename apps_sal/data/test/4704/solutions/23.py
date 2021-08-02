n = int(input())
a = list(map(int, input().split()))

t = sum(a)
m = 10**9
flag = 0
for i in range(len(a) - 1):
    t -= 2 * a[i]
    if i == 0:
        m = abs(t)
    else:
        m = min(abs(t), m)
print(m)
