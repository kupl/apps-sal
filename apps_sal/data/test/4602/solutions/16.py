n = int(input())
k = int(input())
li = list(map(int,input().split()))
total = 0
for i in range(n):
    total += 2*min(li[i],k-li[i])
print(total)
