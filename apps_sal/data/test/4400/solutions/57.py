s = 0
wealth = input()
for i in wealth:
    if i == 'R':
        s = s + 1
    if s >= 2 and wealth[1] == 'S':
        s = 1
print(int(s))
