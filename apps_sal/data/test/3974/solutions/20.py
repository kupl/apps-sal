s = list(input())
ans = 0
while s.count('+') != 0 and s.count('-') != 0:
    flag = 0
    ans += 1
    if s.index('+') < s.index('-'):
        s[s.index('+')] = 0
        for i in range(1, len(s)):
            if flag == 0 and s[i] == '-':
                flag = 1
                s[i] = 0
            elif flag == 1 and s[i] == '+':
                flag = 0
                s[i] = 0
    elif s.index('-') < s.index('+'):
        s[s.index('-')] = 0
        for i in range(1, len(s)):
            if flag == 0 and s[i] == '+':
                flag = 1
                s[i] = 0
            elif flag == 1 and s[i] == '-':
                flag = 0
                s[i] = 0
print(max(ans + s.count('+'), ans + s.count('-')))

