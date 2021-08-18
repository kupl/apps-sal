def ok(k):
    D = {}
    for i in range(n - k + 1):
        s = S[i:i + k]
        try:
            if D[s] + k <= i:
                return True
        except:
            D[s] = i
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
