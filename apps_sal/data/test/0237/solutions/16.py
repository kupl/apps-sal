n, m, k = list(map(int, input().split()))
s = 0
m -= n
s += 1
if m == 0:
    print(1)
    return
while m >= 0:
    if k > s and n - k + 1 > s and m >= 2 * (s - 1) + 1:
        m -= 2 * (s - 1) + 1
    elif k > s and m >= n - k + s:
        m -= n - k + s
    elif n - k + 1 > s and m >= k + s - 1:
        m -= k + s - 1
    elif m >= n:
        s += m // n
        m -= n * (m // n)
        print(s)
        return
    else:
        break
    s += 1
print(s)
