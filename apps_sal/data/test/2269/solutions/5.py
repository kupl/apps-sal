t = int(input())
for _ in range(t):
    s = input()
    a = -1
    b = -1
    c = -1
    mn = 10 ** 9
    for i in range(len(s)):
        if s[i] == '1':
            a = i
        elif s[i] == '2':
            b = i
        else:
            c = i
        if a != -1 and b != -1 and c != -1:
            mn = min(mn, max(a, b, c) - min(a, b, c) + 1)
    if mn == 10 ** 9:
        print(0)
    else:
        print(mn)


