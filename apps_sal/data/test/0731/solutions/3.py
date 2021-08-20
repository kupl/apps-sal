(w, m, k) = map(int, input().split())
L = len(str(m))
end = m
flag = False
while True:
    if w > (10 ** L - end) * k * L:
        w -= (10 ** L - end) * k * L
        end = 10 ** L
        L += 1
    else:
        end += w // (L * k)
        break
if not flag:
    print(end - m)
