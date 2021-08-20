n = int(input())
t = input()
s = '110'
com = ''
a = -(-(n * 2) // 3)
for i in range(a):
    com += s
count = 0
for i in range(a * 3 - n + 1):
    if com[i:n + i] == t:
        count += 1
if count == 0:
    print(0)
elif len(com) <= 3:
    print(pow(10, 10) * count)
else:
    print(pow(10, 10) - (a - count))
