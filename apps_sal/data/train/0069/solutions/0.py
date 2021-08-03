t = int(input())

for case in range(t):
    a, b = list(map(int, input().split()))
    s = input()

    z = 10000
    total = 0
    act = False

    for i in range(len(s)):
        cur = s[i]
        if cur == '0':
            z += 1
            act = False
        else:
            if not act:
                act = True
                total += min(a, b * z)
                z = 0

    print(total)
