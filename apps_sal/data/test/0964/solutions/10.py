def print_if_possible(w, h):
    xw, xh = max(w), max(h)
    nw, nh = min(w), min(h)
    x = max(xw, xh)
    wm, hm = w.count(xw), h.count(xh)
    if hm == 1 and xh == x:
        q = h.index(xh)
        i, j = (q+1)%3, (q+2)%3
        if xh != sum(w)-w[i] or h[q] != h[i] + h[j] or w[i]!=w[j]:
            return False
        print(x)
        for yi in range(h[i]):
            print("%s%s" % (("ABC"[i])*w[i], ("ABC"[q])*w[q]))
        for yi in range(h[j]):
            print("%s%s" % (("ABC"[j])*w[j], ("ABC"[q])*w[q]))
        return True
    elif wm == 1 and xw == x:
        q = w.index(xw)
        i, j = (q+1)%3, (q+2)%3
        if xw != sum(h)-h[i] or w[q] != w[i] + w[j] or h[i]!=h[j]:
            return False
        print(x)
        for yi in range(h[i]):
            print("%s%s" % (("ABC"[i])*w[i], ("ABC"[j])*w[j]))
        for yi in range(h[q]):
            print(("ABC"[q])*w[q])
        return True
    elif wm == 3 and xw == sum(h):
        q = w.index(xw)
        i, j = (q+1)%3, (q+2)%3
        print(x)
        for yi in range(h[i]): print(("ABC"[i])*w[i])
        for yi in range(h[j]): print(("ABC"[j])*w[j])
        for yi in range(h[q]): print(("ABC"[q])*w[q])
        return True
    elif hm == 3 and xh == sum(w):
        q = h.index(xh)
        i, j = (q+1)%3, (q+2)%3
        print(x)
        for yi in range(h[i]):
            print("%s%s%s" % (("ABC"[i])*w[i], ("ABC"[j])*w[j], ("ABC"[q])*w[q]))
        return True
    else:
        return False

def rec(i, w, h):
    if i == 3:
        if print_if_possible(w, h):
            return
        return
    rec(i+1, w, h)
    w[i], h[i] = h[i], w[i]
    rec(i+1, w, h)
    w[i], h[i] = h[i], w[i]

w, h = [0, 0, 0], [0, 0, 0]
w[0], h[0], w[1], h[1], w[2], h[2] = [int(i) for i in input().split()]
rec(0, w, h)
print(-1)
