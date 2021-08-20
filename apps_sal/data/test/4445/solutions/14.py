import heapq
n = int(input())
arr = list(map(int, input().split()))
ch = []
nc = []
for i in arr:
    if i % 2 == 0:
        ch.append(i)
    else:
        nc.append(i)
if len(ch) > len(nc):
    ans = sum(sorted(ch)[:len(ch) - len(nc) - 1])
elif len(ch) < len(nc):
    ans = sum(sorted(nc)[:len(nc) - len(ch) - 1])
else:
    ans = 0
print(ans)
