a = []
n = int(input())
a += (int(i) for i in input().split())
r, m = 1, 1
while m != 0:
    m2 = m
    m = 0
    for i in range(n):
        if a[i] % r == 0:
            m += 1
    if m != 0:
        r = r * 2
    else:
        break
print(r // 2, m2)
