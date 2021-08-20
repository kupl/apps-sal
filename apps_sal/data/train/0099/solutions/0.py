for _ in range(int(input())):
    n = int(input())
    s = input()
    l = 0
    r = n - 1
    if s.count('0') == n:
        print(s)
        continue
    if s.count('1') == n:
        print(s)
        continue
    while s[l] == '0':
        l += 1
    while s[r] == '1':
        r -= 1
    if r <= l:
        print(s)
        continue
    print(l * '0' + '0' + (n - r - 1) * '1')
