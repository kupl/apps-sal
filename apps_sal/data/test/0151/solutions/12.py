gl = ["a", "e", "i", "o", "u"]


def mist(a, b, c):
    if a in gl or b in gl or c in gl:
        return False
    if a == b and b == c:
        return False
    return True


s = input()
n = len(s)
if n == 1:
    print(s[0])
else:
    print(s[0] + s[1], end='')
    last1 = s[0]
    last2 = s[1]
    for i in range(2, n):
        now = s[i]
        if now in gl:
            print(now, end='')
            last1, last2 = last2, now
            continue
        if mist(last1, last2, now):
            print(" " + now, end='')
            last1 = "a"
            last2 = now
        else:
            print(now, end='')
            last1, last2 = last2, now
