n = int(input())
AB = [tuple(map(int,input().split())) for i in range(n)]

l = [-1]*(2*n+1)
m = 0

for k  in range(n):
    i,j = AB[k]
    if i == -1 and j == -1:
        m += 1
        continue
    if i == -1:
        if l[j]>=0:
            print("No")
            return
        l[j] = k
        continue
    if j == -1:
        if l[i]>=0:
            print("No")
            return
        l[i] = k
        continue
    if i >= j or j-i > n:
        print("No")
        return
    if l[j]>=0:
        print("No")
        return
    l[j] = k
    if l[i]>=0:
        print("No")
        return
    l[i] = k

dp = [-1]*(2*n+1)
dp[0] = m
for i in range(1,2*n+2,2):
    #print(dp)
    if dp[i-1] == -1:
        continue
    for j in range(i+2,2*n+2,2):
        
        x = dp[i-1]
        count = [0]*(2*n+1)
        dif = (j-i)//2
        for k in range(n):
            a,b = AB[k]
            if a == b == -1:
                continue
            if a == -1:
                if i+dif <= b < j:
                    if count[b] or count[b-dif]:
                        continue
                    count[b] += 1
                    count[b-dif] += 1
            elif b == -1:
                if i <= a < i+dif:
                    if count[a] or count[a+dif]:
                        continue
                    count[a] += 1
                    count[a+dif] += 1
            else:
                if i <= a < i+dif and a+dif == b:
                    if count[a] or count[b]:
                        continue
                    count[a] += 1
                    count[a+dif] += 1
        if x*2 >= j-i-sum(count):
            dp[j-1] = max(dp[j-1],x-(j-i-sum(count))//2)

if dp[-1] >= 0:
    print("Yes")
else:
    print("No")
