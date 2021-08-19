(s, p) = map(int, input().split())
ans = 'No'
for i in range(1, 1000050):
    if i * (s - i) == p:
        ans = 'Yes'
        break
print(ans)
