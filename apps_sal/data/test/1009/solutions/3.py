
n, k = list(map(int, input().split(" ")))
l = list(map(int, input().split(" ")))

li = []

for i in range((n-k-1)+1):
    li.append(l[i] + l[2*(n-k-1)+1 - i])

if(len(li) == 0):
    print(l[n-1])
else:        
    print(max(max(li), l[n-1]))

