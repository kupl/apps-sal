def Count (n):
    cnt = 0
    x = 1
    while True:
        if x > n:
            break
        y = 1
        while True:
            if x * y > n:
                break
            cnt += 1
            y *= 3
        x *= 2
    return cnt

def Result (l, r):
    if l == 0:
        return Count (r)
    return Count (r) - Count (l - 1)

l, r = map (int, input ().split ())
print (Result (l, r))
