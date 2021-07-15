n = int(input())
a = list(map(int, input().split()))
b = [0]
c = [0, 0]
for i in range(0, n, 2):
    b.append(b[-1] + a[i])
    b.append(b[-1])
    if (i + 1 < n):
        c.append(c[-1] + a[i + 1])
        c.append(c[-1])
#print(b)
#print(c)
ans = 0
for i in range(n):
    k1 = 0
    k2 = 0
    k1 += b[i] + c[n] - c[i + 1]
    k2 += c[i] + b[n] - b[i + 1]
    #print(i, k1, k2)
    if (k1 == k2):
        ans += 1
print(ans)
