li = list('abcdefghijknmlopqrstuvwxyz')
S = list(input())
ans = 'None'
for l in li:
    if not l in S:
        ans = l
        break
print(ans)
