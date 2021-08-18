N, M = list(map(int, input().split()))
SC = [list(map(int, input().split())) for _ in range(M)]

condition = [False] * N
ans = '-1'
invalid = False

for s, c in SC:
    dig = s - 1
    if str(condition[dig]) == 'False':
        condition[dig] = c
    elif condition[dig] != c:
        invalid = True


if str(condition[0]) == '0':
    if M > 1:
        invalid = True

for i in range(N):
    if str(condition[i]) == 'False':
        if i == 0:
            condition[i] = 1
        else:
            condition[i] = 0

if condition[0] != 0 and not invalid:
    ans = ''
    for num in condition:
        ans += str(num)
elif condition[0] == 0 and not invalid and N == 1:
    ans = ''
    for num in condition:
        ans += str(num)

if M == 0:
    if N == 1:
        ans = '0'
    else:
        ans = '1'
        for i in range(N - 1):
            ans += '0'

print(ans)
