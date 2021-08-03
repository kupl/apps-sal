x = int(input())
line = input().split()
h = int(line[0])
m = int(line[1])
s = 0
while (not m % 10 == 7) and (not h % 10 == 7):
    m -= x
    if m < 0:
        m += 60
        h -= 1
    if h < 0:
        h += 24
    s += 1
print(s)
