def ok(l):
    D = {}
    for i in range(n - l + 1):
        h = hash(S[i:i + l])
        try:
            if D[h] + l <= i:
                return True
        except:
            D[h] = i
    return False


n = int(input())
S = input()
l, r = 0, n + 1
while r - l > 1:
    c = (l + r) // 2
    if ok(c):
        l = c
    else:
        r = c
print(l)
