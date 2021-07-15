n, L, a = list(map(int, input().split()))
x = [0]
for i in range(n):
    t, l = list(map(int, input().split()))
    x.append(t)
    x.append(t+l)

x.append(L)

res = 0
for i in range(0, len(x), 2):
    res += (x[i+1]-x[i])//a

print(res)

