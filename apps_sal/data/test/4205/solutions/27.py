N = int(input())
lsp = list(map(int,input().split()))
ii = 0
for i in range(N):
    if i+1 == lsp[i]:
        continue
    ii += 1
if ii >2:
    print('NO')
else:
    print('YES')
