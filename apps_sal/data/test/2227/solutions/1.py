L = input().split('heavy')
ans = 0
for i in range(len(L)):
    ans += i * L[i].count('metal')
print(ans)
