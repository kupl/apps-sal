n=int(input())
s=input()
t=input()

result = 0
out = []
ab=ba=-1
for i in range(n):
    if s[i]==t[i]:
        continue
    if s[i]=='a' and t[i]=='b':
        if ab != -1:
            out.append((ab+1,i+1))
            result += 1
            ab = -1
        else:
            ab = i
    else:
        if ba != -1:
            out.append((ba+1,i+1))
            result += 1
            ba = -1
        else:
            ba = i

if (ab == -1) != (ba == -1):
    print(-1)
elif (ab == ba == -1):
    print(result)
    for i,j in out:
        print(i,j)
else:
    print(result+2)
    for i,j in out:
        print(i,j)
    print(ab+1,ab+1)
    print(ab+1,ba+1)

