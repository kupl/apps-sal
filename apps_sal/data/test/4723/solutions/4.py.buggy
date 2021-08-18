s = input()[::-1]
t = input()[::-1]


def match(string, substring):
    for a, b in zip(string, substring):
        if a == '?':
            continue
        if a != b:
            return False
    return True


# なるべく後方で一致させる
LEN_S = len(s)
LEN_T = len(t)
ans = ''
for i in range(LEN_S - LEN_T + 1):
    sub = s[i:i + LEN_S]
    if match(sub, t):
        ans = s[:i] + t + s[i + LEN_T:]
        ans = ans[::-1].replace('?', 'a')
        break
else:
    print('UNRESTORABLE')
    return

print(ans)
