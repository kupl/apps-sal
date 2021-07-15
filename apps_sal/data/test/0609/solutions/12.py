n = int(input())
d = 1
k = 0
for i in range(n):
    s = input()
    if d == 1:
        if k == 0:
            k = 1
            if s[1]*(n-2) == s[1:(n-1)] and s[0] == s[n-1]:
                c = s[1]
                b = s[0]
            else:
                d = 0
        elif c == b:
            d = 0
        else:
            j = i
            if i > n//2:
                j = n-i-1
            if i == n//2:
                if s != c*j + b + c*(n-j-1):
                    d = 0
            elif s != c*j + b + c*(n-2*j-2) + b + c*j:
                d = 0
                #print(i,j,s, c*j + b + c*(n-2*j-2) + b + c*j)
if d == 1:
    print('YES')
else:
    print('NO')
