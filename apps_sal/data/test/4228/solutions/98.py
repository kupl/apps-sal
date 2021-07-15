import sys

n,l = map(int,input().split())

taste_list = [l+x-1 for x in range(1,n+1)]
taste_sum = sum(taste_list)
diff = sys.maxsize

for i in range(n):
    if diff>abs(taste_list[i]):
        diff = abs(taste_list[i])
        num = i
    
print(taste_sum-taste_list[num])
