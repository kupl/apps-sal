jump = ['A', 'E', 'I', 'O', 'U', 'Y']

ans = 1
s = input()
j = 1
for i in s:
    if i in jump:
        ans = max(ans, j)
        j = 0
    j += 1
ans = max(ans, j)
print(ans)
