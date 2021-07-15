T = int(input())

def solve(s):
    kb = list()
    cursor = -1
    seen = set()
    for c in s:
        if c in seen:
            if cursor - 1 >= 0 and kb[cursor - 1] == c:
                cursor -= 1
            elif cursor + 1 < len(kb) and kb[cursor + 1] == c:
                cursor += 1
            else:
                print('NO')
                return
        else:
            if cursor not in [0, len(kb) - 1]:
                print('NO')
                return
            elif cursor == 0:
                kb.insert(0, c)
                cursor = 0
            else:
                kb.append(c)
                cursor = len(kb) - 1
            seen.add(c)
    print('YES')
    ans = ''.join(kb)
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in seen:
            ans += c
    print(ans)

for _ in range(T):
    solve(input())
