N = int(input())
*A, = list(map(int, input().split()))
mx = -float('inf')
mn = float('inf')
mxi = mni = -1
for i, a in enumerate(A, 1):
    if mx < a:
        mx, mxi = a, i
    if mn > a:
        mn, mni = a, i
ans = []
if abs(mx) >= abs(mn):
    for i in range(1, N + 1):
        if i == mxi: continue
        ans.append(f'{mxi} {i}')
    for i in range(1, N):
        ans.append(f'{i} {i+1}')
else:
    for i in range(1, N + 1):
        if i == mni: continue
        ans.append(f'{mni} {i}')
    for i in range(N, 1, -1):
        ans.append(f'{i} {i-1}')
print((len(ans)))
print(('\n'.join(map(str, ans))))
