n = int(input())
f = [1,1]
for i in range(n):
    f.append(f[-1]+f[-2])
f = set(f)
ans = []
for i in range(1, n+1):
    if i in f:
        ans.append('O')
    else:
        ans.append('o')
print(''.join(ans))
