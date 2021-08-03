x = 0
mx = 0
n = int(input())
s = input()

for c in s:
    if c == 'I':
        x += 1
    else:
        x -= 1
    mx = max(mx, x)

print(mx)
