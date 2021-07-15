s = input()
name = False
s2 = '0'
cnt = 0
pointsPresent = False
sum = 0
for i in range(len(s)):
    if s[i] in "1234567890.":
        name = False
    else:
        name = True
    if name:
        if cnt == 3 or not pointsPresent:
            sum += int(s2) * 100
        else:
            sum += int(s2)
        s2 = "0"
        cnt = 0
        pointsPresent = False
    else:
        if s[i] != '.':
            s2 += s[i]
            cnt += 1
        else:
            cnt = 0
            pointsPresent = True
if cnt == 3 or not pointsPresent:
    sum += int(s2) * 100
else:
    sum += int(s2)

if sum < 10:
    print("0.0" + str(sum))
elif sum < 100:
    print("0." + str(sum))
else:
    if sum % 100 == 0:
        sum //= 100
        c = -1
    else:
        c = 0
    s3 = str(sum)
    for i in range(len(s3) - 1, -1, -1):
        c += 1
        if c == 3:
            c = 0
            s3 = s3[:i + 1] + '.' + s3[i + 1:]
    print(s3)
