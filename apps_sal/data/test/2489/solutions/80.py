n = int(input())
a = list(map(int,input().split()))

ma = max(a)
m = [0]*(ma + 1)

for i in a:
    if m[i] == 1:
        m[i] = 2
        continue
    for j in range(i,ma+1,i):
        m[j]+=1
ans = 0
for i in a:
    if m[i] == 1:
        ans += 1
print(ans)
