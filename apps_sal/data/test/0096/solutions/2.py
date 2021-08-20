(n, k) = list(map(int, input().split()))
s = bin(n)[2:]
ans = 1
if k == 1:
    ans = n
else:
    f = len(s)
    for d in range(1, f):
        rgt = int(s[-d:], 2)
        lft = int(s[:-d], 2)
        c = 2 ** d
        if rgt + c >= k:
            if rgt + c > k:
                ans = max(lft * 2, ans)
            else:
                ans = max(lft, ans)
        if 2 * c - 1 >= k:
            if 2 * c - 1 > k:
                ans = max((lft - 1) * 2, ans)
            else:
                ans = max(lft - 1, ans)
print(ans)
