q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = True
    S = -1
    i = 0
    for j in range(n):
        if a[i] == a[i + 1] and a[-(1 + i)] == a[-(2 + i)]:
            if S == -1 or S == a[i] * a[-(1 + i)]:
                S = a[i] * a[-(1 + i)]
            else:
                ans = False
                break
        else:
            ans = False
            break
        i += 2
    if ans:
        print('YES')
    else:
        print('NO')
