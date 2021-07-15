n, s = int(input()), input()
a = [int(i) for i in input().split()]
c = i = 0
while True:
    if s[i] == '>':
        i += a[i]
    else:
        i -= a[i]
    if i < 0 or i >= n:
        print("FINITE")
        return
    c += 1
    if c > n:
        print("INFINITE")
        return
