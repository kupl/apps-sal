s = input()
ans = eval(s)
for i in range(len(s)-1):
    if s[i] == "*":
        k = "(" + s[0:i] + ")" + s[i:len(s)]
        t = eval(k)
        if t > ans:
            ans = t
        k = s[0:i+1] + "(" + s[i+1:len(s)] + ")"
        t = eval(k)
        if t > ans:
            ans = t
        for j in range(i+2, len(s)):
            if s[j] == "*":
                k = s[0:i+1] + "(" + s[i+1:j] + ")" + s[j:len(s)]
                t = eval(k)
                if t > ans:
                    ans = t
print(ans)
