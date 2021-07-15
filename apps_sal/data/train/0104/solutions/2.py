import sys

T = int(sys.stdin.readline().strip())
Q = []
P = [0] * (10 ** 6)
for i in range (2, 2 * 10 ** 5 + 10):
    v = True
    if P[i] == 0:
        Q.append(i)
        j = i
        while j < 10 ** 6:
            P[j] = 1
            j = j + i

def factors(n):
    i2 = 0
    ans = [1]
    while n > 1:
        m = 0
        while n % Q[i2] == 0:
            m = m + 1
            n = n // Q[i2]
        ans2 = []
        for h in range (0, m+1):
            for j in ans:
                ans2.append(j * (Q[i2] ** h))
        i2 = i2 + 1
        ans = ans2[:]
    return ans

for t in range (0, T):
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().strip().split()))
    c = list(map(int, sys.stdin.readline().strip().split()))
    for i in range (0, n):
        p[i] = p[i] - 1
    P = []
    L = []
    i = 0
    ans = n
    while i < n:
        if p[i] == -1:
            i = i + 1
        else:
            j = i
            x = [j]
            while p[j] != i:
                x.append(p[j])
                j2 = p[j]
                p[j] = -1
                j = j2
            p[j] = -1
            P.append(x)
            l = len(x)
            F = factors(l)
            for f in F:
                for j in range (0, f):
                    v = True
                    for h in range (0, l // f):
                        if c[x[j + h * f]] != c[x[j]]:
                            v = False
                    if v == True:
                        ans = min(ans, f)   
    print(ans)


