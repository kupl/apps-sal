N = int(input())
S = input()
lb = 0
rb = N + 1
while rb - lb > 1:
    mid = (lb + rb) // 2
    x = 0
    for (i, s) in enumerate(S[:mid]):
        x += pow(26, i) * (ord(s) - ord('a'))
    m = pow(26, mid - 1)
    a = [x]
    for (i, s) in enumerate(S[mid:]):
        x -= ord(S[i]) - ord('a')
        x //= 26
        x += m * (ord(s) - ord('a'))
        a += [x]
    f = 0
    se = set([])
    for (i, x) in enumerate(a):
        if i >= mid:
            se.add(a[i - mid])
        if x in se:
            f = 1
            break
    if f:
        lb = mid
    else:
        rb = mid
print(lb)
