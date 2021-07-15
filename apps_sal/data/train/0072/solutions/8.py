def Solve(nCase):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    l = list(set(a))
    p = len(l)
    if p > k:
        print(-1)
        return
    for i in range(k - p):
        l.append(a[0])
    ans = n * l
    print(len(ans))
    print(' '.join(str(x) for x in ans)) 


T = int(input())
for i in range(1, T + 1):
    Solve(i)

