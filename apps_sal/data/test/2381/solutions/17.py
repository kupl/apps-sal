N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
M = []
m = []
for a in A:
    if a < 0:
        m.append(abs(a))
    else:
        M.append(a)

i = 0
j = 0
tmp = 1
P = 10**9 + 7

if (K % 2 == 0 and (len(m) // 2 * 2 + len(M) // 2 * 2) >= K) or (K % 2 == 1 and (len(M) + len(m) // 2 * 2) >= K and len(M) > 0):
    m.sort(reverse=True)
    M.sort(reverse=True)
    while K > 0:
        if K >= 2:
            if j + 2 <= len(M) and i + 2 <= len(m):
                if m[i] * m[i + 1] < M[j] * M[j + 1]:
                    tmp *= M[j]
                    j += 1
                    K -= 1
                else:
                    tmp *= m[i] * m[i + 1]
                    i += 2
                    K -= 2
            elif j + 2 <= len(M):
                tmp *= M[j]
                j += 1
                K -= 1
            elif i + 2 <= len(m):
                tmp *= m[i] * m[i + 1]
                i += 2
                K -= 2
            else:
                tmp *= m[i] * M[j]
        else:
            tmp *= M[j]
            K -= 1
        tmp %= P
else:
    m.sort()
    M.sort()
    for _ in range(K):
        if j + 1 <= len(M) and i + 1 <= len(m):
            if M[j] < m[i]:
                tmp *= M[j]
                j += 1
            else:
                tmp *= m[i]
                i += 1
        elif j + 1 <= len(M):
            tmp *= M[j]
            j += 1
        else:
            tmp *= m[i]
            i += 1
        tmp %= P
    tmp *= -1
    tmp %= P

print(tmp)
