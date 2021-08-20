s1 = input()
s2 = input()
s3 = input()
s4 = input()
i = 0
f = False
while i < 3 and f == False:
    if s1[i] == s2[i] and s1[i + 1] == s2[i + 1] == s1[i] or (s1[i] == s2[i] and s1[i + 1] != s2[i + 1]) or (s1[i] != s2[i] and s1[i + 1] == s2[i + 1]):
        f = True
    i += 1
i = 0
while i < 3 and f == False:
    if s2[i] == s3[i] and s2[i + 1] == s3[i + 1] == s2[i] or (s2[i] == s3[i] and s2[i + 1] != s3[i + 1]) or (s2[i] != s3[i] and s2[i + 1] == s3[i + 1]):
        f = True
    i += 1
i = 0
while i < 3 and f == False:
    if s3[i] == s4[i] and s3[i + 1] == s4[i + 1] == s3[i] or (s3[i] == s4[i] and s3[i + 1] != s4[i + 1]) or (s3[i] != s4[i] and s3[i + 1] == s4[i + 1]):
        f = True
    i += 1
if f:
    print('YES')
else:
    print('NO')
