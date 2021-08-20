n = int(input())
r = 0
for i in range(0, n):
    str = input()
    if str[1] == '+':
        r += 1
    else:
        r -= 1
print(r)
