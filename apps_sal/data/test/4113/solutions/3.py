n = int(input())
ans = 'No'
for i in range(26):
    for j in range(26):
        count = 4 * i + 7 * j
        if count == n:
            ans = 'Yes'
            break
print(ans)
