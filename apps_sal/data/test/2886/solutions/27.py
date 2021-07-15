def abc043_d():
    s = str(input())
    n = len(s)
    ans = (-1, -1)
    if n == 2:
        if s[0] == s[1]:
            ans = (1, 2)
    else:
        for i in range(n-2):
            if len(set(s[i:i+3])) < 3:
                ans = (i+1, i+3)
                break
    print(*ans, sep=' ')

def __starting_point():
    abc043_d()
__starting_point()
