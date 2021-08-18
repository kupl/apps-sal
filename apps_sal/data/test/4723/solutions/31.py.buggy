S0 = input()
T = input()

n, m = len(S0), len(T)
if n < m:
    print("UNRESTORABLE")
    return

start, end = -1, -1
for i in reversed(range(n - m + 1)):
    ok = True
    for j in range(m):
        ok = ok and (S0[i + j] == T[j] or S0[i + j] == '?')
    if ok:
        start = i
        end = i + m - 1
        break

if start >= 0:
    S = ''
    for i in range(n):
        if start <= i <= end:
            S += T[i - start]
        else:
            if S0[i] == '?':
                S += 'a'
            else:
                S += S0[i]
    print(S)
else:
    print("UNRESTORABLE")
