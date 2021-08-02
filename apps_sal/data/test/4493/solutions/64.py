L = [list(map(int, input().split())) for _ in range(3)]
ans = 'Yes'

if L[0][0] + L[1][1] != L[0][1] + L[1][0]: ans = 'No'
if L[0][1] + L[1][2] != L[0][2] + L[1][1]: ans = 'No'
if L[1][0] + L[2][1] != L[1][1] + L[2][0]: ans = 'No'
if L[1][1] + L[2][2] != L[1][2] + L[2][1]: ans = 'No'

print(ans)
