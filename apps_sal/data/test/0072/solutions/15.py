n = int(input())
s1 = input().strip()
s2 = input().strip()
s3 = input().strip()
d1 = [0 for _ in range(52)]
d2 = [0 for _ in range(52)]
d3 = [0 for _ in range(52)]
maxi1 = 0
maxi2 = 0
maxi3 = 0
for i in s1:
    if ord(i) <= 90:
        j = ord(i) - 65
    else:
        j = ord(i) - 97 + 26
    d1[j] += 1
maxi1 = max(d1)
for i in s2:
    if ord(i) <= 90:
        j = ord(i) - 65
    else:
        j = ord(i) - 97 + 26
    d2[j] += 1
maxi2 = max(d2)
for i in s3:
    if ord(i) <= 90:
        j = ord(i) - 65
    else:
        j = ord(i) - 97 + 26
    d3[j] += 1
maxi3 = max(d3)
if maxi1 + n <= len(s1):
    maxi1 += n
elif n == 1:
    maxi1 = len(s1) - 1
else:
    maxi1 = len(s1)
if maxi2 + n <= len(s1):
    maxi2 += n
elif n == 1:
    maxi2 = len(s1) - 1
else:
    maxi2 = len(s1)
if maxi3 + n <= len(s1):
    maxi3 += n
elif n == 1:
    maxi3 = len(s1) - 1
else:
    maxi3 = len(s1)
if maxi1 > maxi2 and maxi1 > maxi3:
    print('Kuro')
elif maxi2 > maxi1 and maxi2 > maxi3:
    print('Shiro')
elif maxi3 > maxi1 and maxi3 > maxi2:
    print('Katie')
else:
    print('Draw')
