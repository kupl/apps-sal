T = int(input())


def solve(S):
    res = [S[0]]
    pos = 0
    for s in S[1:]:
        if 0 <= pos - 1 < len(res) and res[pos - 1] == s:
            pos = pos - 1
        elif 0 <= pos + 1 < len(res) and res[pos + 1] == s:
            pos = pos + 1
        elif pos == 0 and s not in res:
            res.insert(0, s)
        elif pos == len(res) - 1 and s not in res:
            res.append(s)
            pos += 1
        else:
            return None
    for x in range(ord('a'), ord('z') + 1):
        x = chr(x)
        if x not in res:
            res.append(x)
    return ''.join(res)


for _ in range(T):
    res = solve(input())
    if res is None:
        print('NO')
    else:
        print('YES')
        print(res)
