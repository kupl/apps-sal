def main(n, a, b):
    if not a * b >= n >= a + b - 1:
        return [-1]
    ans = []
    flg = False
    for x in range(b):
        if not flg:
            for y in range(a):
                ans.append(b - x + b * y)
                if len(ans) + (b - x) == n:
                    if y != a - 1:
                        ans.append(b - x + b * (a - 1))
                    else:
                        ans.append(b - (x + 1))
                    flg = True
                    break
        elif flg:
            ans.append(b - x + b * (a - 1))
    c = ans.copy()
    c.sort()
    from bisect import bisect_right
    ans = [bisect_right(c, x) for x in ans]
    return ans


(n, a, b) = map(int, input().split())
ary = main(n, a, b)
print(*ary, sep=' ')
