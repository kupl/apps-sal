n = int(input())
s = ''


def getch(i):
    if i % 4 == 0 or i % 4 == 1:
        return 'a'
    else:
        return 'b'


for i in range(n):
    s += getch(i)
print(s)
