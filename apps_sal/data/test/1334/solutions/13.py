from sys import stdin as cin


def main():
    n, m = map(int, input().split())
    s = input()
    q = set()
    c = 'z'
    x = 'a'
    for i in s:
        q.add(i)
        if ord(c) > ord(i):
            c = i
        if ord(x) < ord(i):
            x = i
    if n >= m:
        s = s[:m]
        for i in range(m - 1, -1, -1):
            if s[i] != x:
                print(s[:i], end='')
                w = 1 + ord(s[i])
                while chr(w) not in q:
                    w += 1
                print(chr(w) + c * (m - i - 1))
                return
# for i in range(m):
# if i < n and s[i] in q:
# q.remove(s[i])
# if len(q) == 1:
##                    print(*q, end = '')
# elif len(q) == 0:
##                    print(c, end = '')
# else:
##                    print(s[i], end = '')
# else:
# if i < n and len(q) <= 1:
##                    print(c, end = '')
# else:
##                    print(s[i], end = '')
    else:
        print(s + c * (m - n))


main()
