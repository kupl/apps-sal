n = int(input())
a = list(map(int,input().split()))
b = [0]*n
ans = []    
for i in range(n-1, -1, -1):
    if sum(b[i::i+1])%2 != a[i]:
        b[i] = 1
        ans.append(i+1)
print(len(ans))
if len(ans):
    print(*ans)
