def go(n, m):
    t = 2**(n-1)
    if m == t:
        return n
    else:
        if m < t:
            return go(n-1, m)
        else:
            return go(n-1, m-t)
n, m = map(int, input().split())
print(go(n, m))
