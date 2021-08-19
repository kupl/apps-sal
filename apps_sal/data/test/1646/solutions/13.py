n = int(input())
s = input()
k = 0
for x in s:
    if x == '0':
        k += 1
if s != '0':
    print('1' + '0' * k)
else:
    print(s)
