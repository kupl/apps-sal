from collections import defaultdict
N = int(input())
if(N == 1):
    print(0)
    return
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
Dict = defaultdict(int)
Sum = defaultdict(int)
for i in range(N):
    Dict[a[i]] += 1
    Sum[a[i]] += b[i]
ans = 0
val = 0
Group = []
for i in Dict.keys():
    if(Dict[i] > 1):
        Group.append(i)
        ans += Sum[i]
        val |= i
for i in range(N):
    if(Dict[a[i]] == 1):
        for k in Group:
            if(a[i] | k <= k):
                ans += Sum[a[i]]
                break
print(ans)
