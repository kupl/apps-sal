n = int(input())
r = 1
last = ''
for i in range(n):
    inp = input()
    if inp == last:
        x += 1
    else:
        x = 1
    r = max(r, x)
    last = inp
print(r)
