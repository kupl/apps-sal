n,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
sum = 0
for i in range(k):
    sum += li[i]
print(sum)
