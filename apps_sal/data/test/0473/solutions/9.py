s = input()
t1 = (10 * int(s[0]) + int(s[1])) * 60 + (10 * int(s[3]) + int(s[4]))
s = input()
t2 = (10 * int(s[0]) + int(s[1])) * 60 + (10 * int(s[3]) + int(s[4]))
t1 = (t1 - t2 + 24 * 60) % (24 * 60)
x1 = t1 // 60
x2 = t1 % 60
print(x1 // 10, end='')
print(x1 % 10, end='')
print(':', end='')
print(x2 // 10, end='')
print(x2 % 10)
