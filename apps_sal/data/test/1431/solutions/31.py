n = int(input())
a = list(map(int, input().split()))
b = [0] * n
ans = 0
for i in range(n)[::-1]:
    t = 0
    j = (i + 1) * 2
    while j <= n:
        t += b[j - 1]
        j += i + 1
    if a[i] == 0:
        if t % 2 == 0:
            b[i] = 0
        else:
            b[i] = 1
            ans += 1
    elif t % 2 == 0:
        b[i] = 1
        ans += 1
    else:
        b[i] = 0
print(ans)
l = []
for i in range(n):
    if b[i] == 1:
        l.append(str(i + 1))
print(' '.join(l))
