n = int(input())
used = list((input() for x in range(n)))
ans = 'Yes'
for i in range(n - 1):
    if used.count(used[i]) == 2:
        ans = 'No'
        break
    if used[i][-1] != used[i + 1][0]:
        ans = 'No'
print(ans)
