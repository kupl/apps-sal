N = int(input())
a = list(map(int,input().split()))
k = 1
ans = 0
for i in a:
    if i == k:
        k += 1
    else:
        ans +=1
if ans == N:
    ans = -1
print(ans)
