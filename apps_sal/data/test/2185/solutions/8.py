for TT in range(1, int(input()) + 1):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    c = [y - x for x, y in zip(a, b)]
    i = 0
    while i < n and c[i] == 0: i += 1
    j = i
    while j < n and c[j] == c[i]: j += 1
    k = j
    while k < n and c[k] == 0: k += 1
    res = i == n or (c[i] > 0 and k == n)
    print("YES" if res else "NO")
