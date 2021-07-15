N = int(input())
p = [int(i) for i in input().split()]
r = sorted(p)
for i in range(N):
    for j in range(i+1,N):
        q = []
        for k in range(N):
            if(k == i):
                q.append(p[j])
            elif(k == j):
                q.append(p[i])
            else:
                q.append(p[k])
        if(p == r or q == r):
            print("YES")
            return
print("NO")
