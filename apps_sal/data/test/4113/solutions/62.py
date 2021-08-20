N = int(input())
ans = 'No'
if N % 4 == 0:
    ans = 'Yes'
for i in range(15):
    N = N - 7
    if N < 0:
        break
    if N % 4 == 0:
        ans = 'Yes'
print(ans)
