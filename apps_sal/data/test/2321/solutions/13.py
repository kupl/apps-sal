t = int(input())
for _ in range(t):
    input()
    s = input()
    cl = 0
    for c in s:
        if c == '>':
            break
        cl += 1
    cr = 0
    for c in s[::-1]:
        if c == '<':
            break
        cr += 1
    print(min(cl, cr))
