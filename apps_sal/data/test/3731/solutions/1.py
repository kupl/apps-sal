def main(a, b, l, r):
    qL = (l - 1) // (2 * a + 2 * b)
    rL = (l - 1) % (2 * a + 2 * b) + 1
    qR = (r - 1) // (2 * a + 2 * b)
    rR = (r - 1) % (2 * a + 2 * b) + 1
    if qL == qR:
        if a < rL <= a + b and a < rR <= a + b:
            return 1
        if 2 * a + b < rL and 2 * a + b < rR:
            return 1
        if 1 <= rL <= a and 1 <= rR <= a:
            return rR - rL + 1
        if a + b < rL <= 2 * a + b and a + b < rR <= 2 * a + b:
            return rR - rL + 1
        if 1 <= rL <= a + b and 1 <= rR <= a + b:
            return a - rL + 1
        if a + b < rL and a + b < rR:
            return 2 * a + b - rL + 1
        if a < rL <= a + b and a + b < rR <= 2 * a + b:
            return 1 + rR - (a + b)
        if a < rL <= a + b and 2 * a + b < rR:
            return 1 + a
        if 1 <= rL <= a and a + b < rR <= 2 * a + b:
            ans = a - rL + 1 + max(rR - (a + b + b), 0) + min(b, rR) - max(min(rR, b) - rL + 1, 0)
            return ans
        if 1 <= rL <= a and 2 * a + b < rR:
            return a - rL + 1 + a - max(b - rL + 1, 0)
    elif qL == qR - 1:
        newL = qL * (2 * a + 2 * b) + 1
        newR = (qR + 1) * (2 * a + 2 * b)
        if 1 <= rL <= a + b and a + b + 1 <= rR:
            return a + max(a - b, 0) + int(a <= b)
        if a + b + 1 <= rL <= 2 * (a + b) and 2 * a + 2 * b + 1 <= rR <= a + b:
            return main(a, b, l - (a + b), r - (a + b))
        if 1 <= rL <= a and 1 <= rR <= a:
            return a + max(a - b, 0) + int(a <= b) + rR - max(rR - rL + 1, 0)
        if 1 <= rL <= a and a + 1 <= rR <= a + b:
            return a + max(a - b, 0) + int(a <= b)
        if a + 1 <= rL <= a + b and 1 <= rR <= a:
            return 1 + a
        if a + 1 <= rL <= a + b and a + 1 <= rR <= a + b:
            return 1 + a + max(a - b, 0)
        return main(a, b, l - (a + b), r - (a + b))
    else:
        return a + max(a - b, 0) + int(a <= b)


(a, b, l, r) = [int(item) for item in input().split()]
print(main(a, b, l, r))
