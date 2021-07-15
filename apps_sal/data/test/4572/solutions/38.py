S = list(input())
A = list('abcdefghijklmnopqrstuvwxyz')
ans = 'None'
for a in A:
    if a not in S:
        ans = a
        break
print(ans)
