t = int(input())
for i in range(t):
    n = int(input())
    string = input()
    total = 0
    for c in string:
        if c == '0':
            total += 1
        elif c == '1':
            total += 2
    l = len(string.lstrip('0'))
    r = len(string.rstrip('0'))
    total = max(total, 2 * l, 2 * r)
    print(total)
