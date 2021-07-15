
n = int(input())
a = list(map(int,input().split()))

l1 = [0]
l2 = [0]
r1 = [0]
r2 = [0]

for i in range(n):

    if i % 2 == 0:
        l1.append(l1[-1] + a[i])
        l2.append(l2[-1])
        r1.append(r1[-1])
        r2.append(r2[-1] + a[n-1-i])

    else:
        l1.append(l1[-1])
        l2.append(l2[-1] + a[i])
        r1.append(r1[-1] + a[n-1-i])
        r2.append(r2[-1])

ans = 0
for i in range(n+1):
    ans = max(ans , l1[i]+r1[n-i] , l2[i]+r2[n-i])
print (ans)

