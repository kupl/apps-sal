n = int(input())
str = input()
sit = 0
for i in str:
    if (i == 'x'):
        sit += 1
minutes =  abs(n / 2 - sit)
result = ''
if (minutes == 0):
    result = str
else:
    if (sit >= n /2):
        s = 'X'
    else:
        s = 'x'
    l = minutes
    for i in str:
        t = i
        if t != s and l > 0:
            t = s
            l -= 1
        result += t


print("%d" % minutes)
print(result)

