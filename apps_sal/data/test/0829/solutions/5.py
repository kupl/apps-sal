n = int(input())
s = input()
count1 = 0
count0 = 0
for i in range(n):
    if s[i] == '0':
        count0 += 1
    else:
        count1 += 1
if count0 != count1:
    print(1)
    print(s)
else:
    print(2)
    print(s[:1], s[1:])
