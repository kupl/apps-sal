def solve():
    n = int(input())
    s = input()
    if s.count('<') == 0:
        return 0
    if s.count('>') == 0:
        return 0
    if s[0] == '>':
        return 0
    if s[-1] == '<':
        return 0
    s1 = 0
    s2 = 0
    for i in range(n):
        if s[i] == '<':
            s1 += 1
        else:
            break
    for i in range(n - 1, -1, -1):
        if s[i] == '>':
            s2 += 1
        else:
            break
    return min(s1, s2)


t = int(input())
for i in range(t):
    print(solve())
