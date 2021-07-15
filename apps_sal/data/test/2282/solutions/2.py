n = int(input())
s = input()
l = 0
r = 0
for c in s:
    if c == 'L':
        l -= 1
    else:
        r += 1
print(r - l + 1)
