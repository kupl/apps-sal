n = int(input())
cell = input()
ans = 1
i = 0
if cell[i] == '1':
    while i < n - 1 and cell[i + 1] == '1':
        ans += 1
        i += 1
    if i < n - 1:
        ans += 1
print(ans)
