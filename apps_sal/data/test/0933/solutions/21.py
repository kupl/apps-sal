s1 = input()
s2 = '  '
for c in s1:
    if s2[-1] == c:
        if s2[-2] != c:
            s2 += c
    else:
        s2 += c
s3 = ''
i = 2
s2 += '_+_'
while i < len(s2)-3:
    if s2[i]==s2[i+1] and s2[i+2]==s2[i+3]:
        s3 += s2[i:i+3]
        i = i+3
    else:
        s3 += s2[i]
    i+=1
print(s3)

