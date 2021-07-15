import collections

N = int(input())
a = list(map(int,input().split()))
ans = 0

aa = collections.Counter(a).most_common()
#print(aa)

for i,j in aa:
    if i > j:
        ans += j
    if i < j:
        ans += j-i
    
print(ans)
