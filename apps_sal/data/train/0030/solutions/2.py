t = int(input())

for q in range(t):
    n = int(input())
    s = input()
    a, b = 0, 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            if s[i] == '0':
                a += 1
            else:
                b += 1
    print(max(a, b))

