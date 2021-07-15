N,K = map(int,input().split())
A = list(map(lambda x:int(x)-1,input().split()))
i = 0
visited = set([0])

while K > 0:
    i = A[i]
    K -= 1
    if i in visited:
        break
    visited.add(i)
if K == 0:
    print(i+1)
    return
ls = [i]
j = i
while True:
    j = A[j]
    if j == i:
        break
    ls.append(j)
print(ls[K % len(ls)]+1)
