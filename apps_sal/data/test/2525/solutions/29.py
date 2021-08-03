def resolve():
    s = input()
    query = int(input())
    r = 0
    left = ''
    for i in range(query):
        q = input()
        if q[0] == '2':
            _, f, c = q.split()
            if (int(f) + r) % 2 == 0:
                s += c
            else:
                left += c
        else:
            r = (r + 1) % 2
    print(left[::-1] + s if r == 0 else s[::-1] + left)


resolve()
