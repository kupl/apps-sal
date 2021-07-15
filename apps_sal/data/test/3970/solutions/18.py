n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = set()
for i in arr:
    if i%k: ans.add(i)
    elif i//k not in ans: ans.add(i)
print(len(ans))
