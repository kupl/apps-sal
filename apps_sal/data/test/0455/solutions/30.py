import math


def binary(n, m):
    lst = []
    while n != 0:
        lst.append(n % 2)
        n = n // 2
    lst = lst + [0] * (m - len(lst))
    return list(reversed(lst))


def calc(u, v, m):
    result = ''
    u_binary = binary(u, m)
    v_binary = binary(v, m)
    for i in range(m):
        if u_binary[i] == 1 and v_binary[i] == 1:
            result += 'R'
        elif u_binary[i] == 0 and v_binary[i] == 0:
            result += 'L'
        elif u_binary[i] == 1 and v_binary[i] == 0:
            result += 'U'
        else:
            result += 'D'
    return result


U = []
V = []
N = int(input())
(even, odd) = (0, 0)
M = 0
for p in range(N):
    (x, y) = list(map(int, input().split()))
    u = x + y
    v = x - y
    U.append(u)
    V.append(v)
    M = max(M, abs(u), abs(v))
    if (x + y) % 2 == 0:
        even += 1
    else:
        odd += 1
if even >= 1 and odd >= 1:
    print(-1)
else:
    m = math.floor(math.log2(M)) + 1 if M != 0 else 1
    lst = [2 ** i for i in range(m - 1, -1, -1)]
    if odd == 0:
        lst.append(1)
    print(len(lst))
    print(' '.join(map(str, lst)))
    for (u, v) in zip(U, V):
        u = (u + 2 ** m - 1) // 2
        v = (v + 2 ** m - 1) // 2
        print(calc(u, v, m) + 'R' if odd == 0 else calc(u, v, m))
