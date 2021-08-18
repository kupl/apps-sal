n, d = [int(i) for i in input().split()]
s = input()
i = 0
t = 0
f = 1
while i < n - 1 and f == 1:
    f = 0
    k = i + d
    if k >= n:
        k = n - 1
    for j in range(k, i, -1):
        if s[j] == '1':
            f = 1
            i = j
            t = t + 1
            break
if f == 0:
    print(-1)
else:
    print(t)
