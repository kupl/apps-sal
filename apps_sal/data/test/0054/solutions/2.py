w, m = map(int, input().split())

def isOK(w, m):
    wr = convert_base_w(m, w)
    for i in range(101):
        if wr[i] == 0 or wr[i] == 1:
            continue
        elif wr[i] == w - 1 or wr[i] == w:
            wr[i + 1] += 1
        else:
            return False
    return True

def convert_base_w(m, w):
    wr = [0] * 101
    for i in range(101):
        m, r = divmod(m, w)
        wr[i] = r
    return wr

if isOK(w, m):
    print('YES')
else:
    print('NO')
