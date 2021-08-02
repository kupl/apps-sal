n, d = list(map(int, input().split()))
t = []
ans = 0

for i in range(n):
    c = list(map(int, input().split()))
    t.append(c)

for k in range(0, n - 1):
    for j in range(k + 1, n):
        sumsum = 0
        for l in range(d):
            sumsum += (t[k][l] - t[j][l])**2
        dis = sumsum**(1 / 2)

        if dis.is_integer() == True:
            ans += 1
print(ans)
