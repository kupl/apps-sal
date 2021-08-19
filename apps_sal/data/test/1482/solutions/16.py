(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
s = [False] * (n * k + 1)
for ai in a:
    s[ai] = True
for kid in range(k):
    curN = 1
    print(a[kid], end=' ')
    for num in range(n - 1):
        while s[curN]:
            curN += 1
        s[curN] = True
        print(curN, end=' ')
    print('')
