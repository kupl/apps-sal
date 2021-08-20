N = int(input())
q = input()
if len(set(q)) >= N:
    print('YES')
    chars = list(set(q))
    start = False
    for (index, c) in enumerate(q):
        if c in chars:
            if start is not False:
                print(q[start:index])
            N -= 1
            chars.remove(c)
            if N == 0:
                chars = []
            start = index
    else:
        print(q[start:])
else:
    print('NO')
