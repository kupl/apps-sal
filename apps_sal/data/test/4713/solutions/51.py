n = int(input())
s = input()
x = 0
m = 0
for i in range(n):
    if s[i] == 'I':
        x += 1
        m = max(x, m)
    else:
        x -= 1
print(m)
