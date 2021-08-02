import sys
if False:
    inp = open('B.txt', 'r')
else:
    inp = sys.stdin
count = [0]

a = inp.readline().strip()
b = inp.readline().strip()
for i in range(len(b)):
    count.append(count[i] + int(b[i]))
lengthA = len(a)
lengthB = len(b)
ans = 0
for i in range(lengthA):
    if a[i] == '0':
        ans += count[lengthB + i - lengthA + 1] - count[i]
    else:
        ans += lengthB - lengthA + 1 - count[lengthB + i - lengthA + 1] + count[i]
print(ans)
