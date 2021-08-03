n = int(input())

s = input()
a = [s[0], ]
for i in range(1, n):
    a.append(s[i])
    if((a[-1] == 'U' and a[-2] == 'R') or (a[-1] == 'R' and a[-2] == 'U')):
        a.pop()
        a.pop()
        a.append('D')
print(len(a))
