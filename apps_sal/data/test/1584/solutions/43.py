from bisect import bisect


from bisect import bisect_left

n = int(input())
lis = list(map(int, input().split()))

lis.sort()

cnt = 0
for i in range(n-2):
    a = lis[i]
    for j in range(i+1, n-1):
        b = lis[j]
        tmp = bisect_left(lis, a+b)
        
        cnt += tmp - 1 -j
    

print(cnt)
