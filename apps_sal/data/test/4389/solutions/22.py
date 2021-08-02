t = int(input())
for i in range(t):
    s = input()
    res = s[0]
    for i in range(1, len(s) - 1, 2):
        res += s[i]
    res += s[-1]
    print(res)
