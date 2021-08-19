t = int(input())
for j in range(t):
    n = int(input())
    ans = 9 * (len(str(n)) - 1)
    minx = 10
    s = ''
    for i in range(len(str(n))):
        s += '1'
    ans += n // int(s)
    print(ans)
