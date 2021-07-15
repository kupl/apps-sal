n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

def check(x):
    #print(x)
    z = [0] * n
    temp = 0
    y = 0
    for p in x:
        if p == 0:
            temp += 1
        else:
            z[y] = temp
            y += 1
    #print(z)
    ans = 0
    for a, b, c, d in abcd:
        if z[b-1] - z[a-1] == c:
            ans += d
    return ans

def func(x, s, t):
    if s == m:
        temp = [] + x
        while t < n:
            temp.append(1)
            t += 1
        return check(temp)
    ans = func(x + [0], s+1, t)
    if t == n:
        return ans
    else:
        return max(ans, func(x + [1], s, t+1))

print(func([0], 1, 0))
