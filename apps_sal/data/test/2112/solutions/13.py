def kill(left, a, right, x, k, y):
    g = len(a)
    if g < k:
        if max(a) > max(left, right):
            print(-1)
            return
    if x < y * k:
        return g // k * x + g % k * y
    elif max(a) > max(left, right):
        return x + (g - k) * y
    else:
        return g * y


def main():
    (n, m) = list(map(int, input().split(' ')))
    (x, k, y) = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    i = 0
    j = 0
    g = 0
    M = 0
    while i < n and j < m:
        if a[i] == b[j]:
            if g > 0:
                M += kill(b[j - 1] if j > 0 else 0, a[i - g:i], b[j], x, k, y)
                g = 0
            i += 1
            j += 1
        else:
            i += 1
            g += 1
    if i == n and j < m:
        print(-1)
        return
    g += n - i
    if g > 0:
        M += kill(b[j - 1] if j > 0 else 0, a[n - g:n], b[j] if j < m else 0, x, k, y)
    print(M)


main()
