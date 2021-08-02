n = int(input())
j = -1
first = True
for i in range(1, 1 + n):
    if first:
        j += 2
    else:
        j -= 2
    x = (n - j) // 2
    ans = ''
    for k in range(x):
        ans += '*'
    for k in range(j):
        ans += 'D'
    for k in range(x):
        ans += '*'
    print(ans)
    if j == n:
        first = False
