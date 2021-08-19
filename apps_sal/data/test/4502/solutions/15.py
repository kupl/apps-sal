n = int(input())
a = list(map(int, input().split()))
ans = []
if n % 2 == 1:
    i = n
    while i >= 1:
        ans.append(str(a[i - 1]))
        i -= 2
    i = 2
    while i <= n:
        ans.append(str(a[i - 1]))
        i += 2
    print(' '.join(ans))
else:
    i = n
    while i >= 1:
        ans.append(str(a[i - 1]))
        i -= 2
    i = 1
    while i <= n:
        ans.append(str(a[i - 1]))
        i += 2
    print(' '.join(ans))
