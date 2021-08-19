(n, k) = map(int, input().split())
s = input()
q = ''


def a_win(a, b):
    if a == 'S' and b == 'P':
        return True
    elif a == 'P' and b == 'R':
        return True
    elif a == 'R' and b == 'S':
        return True
    elif a == b:
        return True
    else:
        return False


for _ in range(k):
    if len(s) % 2 == 1:
        s = s * 2
    for i in range(0, len(s), 2):
        if a_win(s[i], s[i + 1]):
            q += s[i]
        else:
            q += s[i + 1]
    s = q
    q = ''
print(s[0])
