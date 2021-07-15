n = int(input())
s = input()
res = ""
i = 0
while (i<len(s)):
    if (len(s)-i)%2==1:
        res += s[i]
    else:
        res = s[i] + res
    i+=1

print(res)

