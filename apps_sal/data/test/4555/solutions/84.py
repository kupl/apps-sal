a, b, k = list(map(int, input().split()))

ans = set()
k = min(k,b-a+1)
for i in range(a, a+k):
    ans.add(i)

for i in range(b, b - k, -1):
    ans.add(i)

ans=sorted(list(ans))

for i in (ans):
    print(i)

