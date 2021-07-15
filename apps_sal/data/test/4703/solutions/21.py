s = list(input())
n = len(s)
ans = 0

for i in range(2**(n-1)):
    temp = s[0]
    for j in range(n-1):
        if i>>j & 1:
            temp += "+" + s[j+1]
        else:
            temp += s[j+1]
    ans += eval(temp)

print(ans)

