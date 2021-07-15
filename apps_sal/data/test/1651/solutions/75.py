s, p = map(int, input().split())
ans = 'No'
for i in range(1, int(p ** 0.5)+1):
    if i * (s - i) == p:
        ans = 'Yes' 
print(ans)
