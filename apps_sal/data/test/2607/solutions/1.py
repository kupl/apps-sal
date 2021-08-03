import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    s = I()
    l = []
    last = 0
    for i in range(len(s)):
        nxt = s[i + 1] if i < len(s) - 1 else 0
        if s[i] == '?':
            for c in 'abc':
                if c != last and c != nxt:
                    l.append(c)
                    last = c
                    break
        else:
            if s[i] == nxt:
                print(-1)
                break
            l.append(s[i])
            last = s[i]
    else:
        print("".join(l))
