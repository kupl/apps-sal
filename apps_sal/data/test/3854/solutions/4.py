
def check(arr, l, s):
    m = []
    for _ in range(l+1) : m.append([1] + [0] * (s))
    m[0][0] = 1
    for i, ei in enumerate(arr, 1):
        for j in range(s+1):
            m[i][j] |= m[i-1][j]
            if j >= ei: 
                m[i][j] |= m[i-1][j-ei]
                m[i][j] |= (m[i-1][j-ei] << ei)
    return [i for i in range(s+1) if (m[-1][s] >> i) & 1]

n, s = map(int, input().split())
l = list(map(int, input().split()))
L = check(l, n, s)
print(len(L))
print(*L, sep=' ')

