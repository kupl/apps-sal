n = int(input())
x = 0

for i in range(n):
    t = input()
    if t[0] != 'X':
        x += t[0] == '+'
    else:
        x += t[2] == '+'
print(2 * x - n)
