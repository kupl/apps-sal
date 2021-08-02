t = int(input())

for _ in range(t):
    s = input()

    cur = 0
    m = 0
    res = 0
    for i, c in enumerate(s):
        if c == "+":
            cur += 1
        else:
            cur -= 1
        if cur < m:
            m = cur
            res += i + 1

    print(res + len(s))
