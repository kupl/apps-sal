import statistics
N= int(input())
min_all=[]
max_all = []
for _ in range(N):
    a,b=list(map(int,input().split()))
    min_all.append(a)
    max_all.append(b)
min_median = statistics.median(min_all)
max_median = statistics.median(max_all)
if N%2:
    ans = max_median - min_median+1
else:
    ans = int((max_median - min_median +0.5)*2)
print(ans)

