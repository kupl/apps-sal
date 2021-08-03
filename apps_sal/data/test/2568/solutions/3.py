def solve():
    s = input()
    min_val = 0
    res = 0
    cur = 0
    for i in range(len(s)):
        if s[i] == '-':
            cur -= 1
        else:
            cur += 1
        if min_val > cur:
            res += (i + 1)
            min_val = cur
    print(res + len(s))


for i in range(int(input())):
    solve()
