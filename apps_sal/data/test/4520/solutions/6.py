import heapq

n,k = list(map(int,input().split()))

llis = [ [] for i in range(2 * (10**5) + 1) ]
rlis = [ [] for i in range(2 * (10**5) + 1) ]
flag = [0] * (2 * (10**5) + 1)

for i in range(n):

    l,r = list(map(int,input().split()))
    
    llis[l].append([i+1,r])
    rlis[r].append([i+1,l])

now = 0
rq = []
ans = []
for i in range(2 * (10 ** 5)):
    
    i += 1

    for j in llis[i]:
        now += 1
        ind = j[0]
        r = j[1]
        flag[ind] = 1
        heapq.heappush(rq,[-1 * r,ind])

    for j in rlis[i-1]:
        
        ind = j[0]
        if flag[ind] == 1:
            now -= 1
            flag[ind] = 0

    while now > k:

        nowq = heapq.heappop(rq)
        ind = nowq[1]

        if flag[ind] == 1:
            ans.append(ind)
            now -= 1
            flag[ind] = 0


print(len(ans))
print(" ".join(map(str,ans)))

        

