b = [False] * 101
x = [0] * 101


def count(w, k1):
    if w == 0:
        return 1
    elif w < 0:
        return 0
    ans = 0
    for i in range(1, k1 + 1):
        if w - i < 0:
            break
        if b[w - i]:
            ans = ans + x[w - i]
        else:
            x[w - i] = count(w - i, k1)
            ans = ans + x[w - i]
            b[w - i] = True
    b[w] = True
    x[w] = ans
    return ans


(n, k, d) = map(int, input().split())
x[0] = 1
ans = count(n, k)
b = [False] * 101
x = [0] * 101
x[0] = 1
ans = ans - count(n, min(k, d - 1))
print(ans % 1000000007)
