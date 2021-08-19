T = int(input())
for t in range(T):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sa = sorted(a)
    sb = sorted(b, reverse=True)
    for i in range(k):
        if sa[i] < sb[i]:
            sa[i] = sb[i]
        else:
            break
    res = sum(sa)
    print(res)
