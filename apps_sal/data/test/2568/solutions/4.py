t = int(input())
for you in range(t):
    res = 0
    s = input()
    n = len(s)
    curr = 0
    for i in range(n):
        if(s[i] == '+'):
            curr += 1
        else:
            curr -= 1
        if(curr < 0):
            res += (i + 1)
            curr = 0
    print(res + n)
