n = int(input())
s = input()
cnt = 0
a = []
for i in range(n):
    a.append(s[i])
    if len(a) >= 3 and a[-3] == 'f' and (a[-2] == 'o') and (a[-1] == 'x'):
        for _ in range(3):
            a.pop()
print(len(a))
