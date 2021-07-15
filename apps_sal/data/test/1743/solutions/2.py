n = int(input())
t = [list(map(int, input().split())) for i in range(3)]
t = list(zip(*t))

F = {}
def g(i, j, k):
    if j - i == 1: return t[i][1]
    a, b, c = t[k]
    t[k] = (b, c, 0)
    s = f(i, j)
    t[k] = (a, b, c)
    return s
    
def f(i, j):
    if (i, j, t[i], t[j - 1]) in F: return F[(i, j, t[i], t[j - 1])]
    if j - i == 1: return t[i][0]
    k = (i + j) // 2
    F[(i, j, t[i], t[j - 1])] = max(f(i, k) + g(k, j, k), g(i, k, k - 1) + f(k, j))
    return F[(i, j, t[i], t[j - 1])]

print(f(0, n)) 
