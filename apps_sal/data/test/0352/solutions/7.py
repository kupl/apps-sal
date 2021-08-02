n = int(input())
a1, b1 = [int(x) for x in input().split()]
a2, b2 = [int(x) for x in input().split()]
a3, b3 = [int(x) for x in input().split()]
ans = [a1, a2, a3]
n -= a1 + a2 + a3
if n >= b1 - a1:
    ans[0] = b1
    n -= b1 - a1
    if n >= b2 - a2:
        ans[1] = b2
        n -= b2 - a2
        ans[2] = min(a3 + n, b3)
    else:
        ans[1] += n
else:
    ans[0] += n
print(' '.join([str(x) for x in ans]))
