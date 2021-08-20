def qp(a, b):
    if b == 0:
        return 1
    ans = qp(a, b // 2)
    if b % 2 == 1:
        return ans * ans % 1000000007 * a % 1000000007
    else:
        return ans * ans % 1000000007


(n, m) = map(int, input().split())
ans = qp(qp(2, m) - 1, n)
print(ans)
