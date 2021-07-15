n,m = map(int,input().split())
a = list(map(int,input().split()))

ex = [0] * m
left = [0] * (2*m)
right = [[0,0] for _ in range(2*m)]

ans = 0
for i in range(n-1):
    a0 = a[i]-1
    a1 = a[i+1]-1
    ans += (a1-a0)%m
    left[a0+1] += 1
    right[a1 + (a0>a1)*m][0] += 1
    right[a1 + (a0>a1)*m][1] += (a1-a0)%m -1

now = left[0]
dif = 0
for i in range(1,2*m):
    dif += now
    ex[i%m] -= dif
    now += left[i] - right[i][0]
    dif -= right[i][1]

ans += min(ex)
print(ans)
