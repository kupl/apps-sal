(n, k) = map(int, input().split())
a = list(map(int, input().split()))
t = 0
s = 0
for i in range(n):
    if a[i] == 1:
        t += 1
    else:
        s += 1
num = 0
for i in range(k):
    (t1, s1) = (t, s)
    for j in range(i, n, k):
        if a[j] == 1:
            t1 -= 1
        else:
            s1 -= 1
    num = max(num, abs(s1 - t1))
print(num)
