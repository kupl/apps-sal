n = str(input())
m = str(input())
ans = 0
for i in range(len(n)):
    if n[i] != m[i]:
        ans+=1
print(ans)
