from sys import stdin, stdout


def update(v, w, s):

    while v <= length:
        l[s][v] += w
        v += (v & (-v))


def get_value(v, s):
    ans = 0

    while v != 0:

        ans += l[s][v]
        v -= (v & (-v))
    return ans


s = list(stdin.readline().strip())
q = int(stdin.readline())
length = len(s)
l = [[0 for i in range(length + 1)] for _ in range(26)]

for i in range(length):
    x = ord(s[i]) - 97
    update(i + 1, 1, x)

for _ in range(q):

    n, m, k = stdin.readline().split()
    if n == '1':
        a = s[int(m) - 1]
        x, y = ord(a) - 97, ord(k) - 97
        update(int(m), -1, x)
        update(int(m), 1, y)
        s[int(m) - 1] = k

    else:
        count = 0
        left, r = int(m), int(k)
        for i in range(26):
            if get_value(r, i) - get_value(left - 1, i) >= 1:

                count += 1
        print(count)
