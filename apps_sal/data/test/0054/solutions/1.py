def f(w, m):
    if m == 0:
        return True
    if m % w == 0:
        return f(w, m // w)
    if (m - 1) % w == 0:
        return f(w, (m - 1) // w)
    if (m + 1) % w == 0:
        return f(w, (m + 1) // w)
    return False


w, m = map(int, input().split())
if f(w, m):
    print("YES")
else:
    print("NO")
