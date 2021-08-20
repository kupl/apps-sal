def period_to_zero(value: str):
    if value == '.':
        return 0
    return value


(H, W) = map(int, input().split())
S = list()
S.append([0] * (W + 2))
for i in range(H):
    s = list()
    s.append(0)
    s.extend(list(map(period_to_zero, list(input()))))
    s.append(0)
    S.append(s)
S.append([0] * (W + 2))
for i in range(1, len(S) - 1):
    s_prev = S[i - 1]
    s_current = S[i]
    s_next = S[i + 1]
    for j in range(1, len(s_current) - 1):
        if s_current[j] != '#':
            s_current[j] = (s_prev[j - 1:j + 2] + s_next[j - 1:j + 2] + [s_current[j - 1], s_current[j + 1]]).count('#')
for i in range(1, len(S) - 1):
    s = S[i]
    print(*s[1:len(s) - 1], sep='')
