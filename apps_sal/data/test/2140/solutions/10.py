string = input()
string = list(string)
Slen = len(string)
m = int(input())
inline = input().split()
a = []
for i in range(m):
    a.append(int(inline[i]))
a.append(Slen // 2 + 1)
a.sort()
changes = [0 for i in range(Slen)]
flag = 0
for i in range(len(a) - 1):
    if flag == 0:
        for j in range(a[i], a[i + 1]):
            (string[j - 1], string[Slen - j - 1 + 1]) = (string[Slen - j - 1 + 1], string[j - 1])
    flag = 1 - flag
for i in range(Slen):
    print(string[i], sep='', end='')
