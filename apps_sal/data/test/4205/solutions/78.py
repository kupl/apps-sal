N = int(input())
p = list(map(int,input().split()))

count = 0
for i in range(N):
    j = i + 1
    if p[i] != j:
        count += 1
if count > 2:
    ans = 'NO'
else:
    ans = 'YES'

print(ans)
