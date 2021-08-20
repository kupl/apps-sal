N = int(input())
S = list(input())
minCount = N
left = 0
right = S.count('E')
for n in range(0, N):
    if n != 0 and S[n - 1] == 'W':
        left += 1
    if S[n] == 'E':
        right -= 1
    if minCount > left + right:
        minCount = left + right
print(minCount)
