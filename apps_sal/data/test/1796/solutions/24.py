
n = int(input())
x = 0

for i in range(n):
    t = input()
    if t[1] == '+':
        x += 1
print(2 * x - n)
