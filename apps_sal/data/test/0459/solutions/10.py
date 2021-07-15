def f(a, b, c, d):
    return a == b == c == d

a = [0]
a.extend(list(map(int, input().split())))
if f(a[13], a[14], a[15], a[16]) and f(a[17], a[18], a[19], a[20]):
    if f(a[6], a[8], a[1], a[3]) and f(a[2], a[4], a[22], a[24]):
        if f(a[21], a[23], a[9], a[11]) and f(a[10], a[12], a[5], a[7]):
            print('YES')
            return
    if f(a[6], a[8], a[9], a[11]) and f(a[10], a[12], a[22], a[24]):
        if f(a[21], a[23], a[1], a[3]) and f(a[2], a[4], a[5], a[7]):
            print('YES')
            return
if f(a[5], a[6], a[7], a[8]) and f(a[21], a[22], a[23], a[24]):
    if f(a[17], a[19], a[1], a[2]) and f(a[3], a[4], a[13], a[15]):
        if f(a[14], a[16], a[11], a[12]) and f(a[9], a[10], a[18], a[20]):
            print('YES')
            return
    if f(a[18], a[20], a[3], a[4]) and f(a[1], a[2], a[14], a[16]):
        if f(a[13], a[15], a[9], a[10]) and f(a[11], a[12], a[17], a[19]):
            print('YES')
            return
if f(a[9], a[10], a[11], a[12]) and f(a[1], a[2], a[3], a[4]):
    if f(a[13], a[14], a[7], a[8]) and f(a[5], a[6], a[19], a[20]):
        if f(a[17], a[18], a[23], a[24]) and f(a[21], a[22], a[15], a[16]):
            print('YES')
            return
    if f(a[15], a[16], a[5], a[6]) and f(a[7], a[8], a[17], a[18]):
        if f(a[19], a[20], a[21], a[22]) and f(a[23], a[24], a[13], a[14]):
            print('YES')
            return
print('NO')
