n = int(input())
m = input()
m = list(m)
if n % 2 == 0:
    d = 0
    for i in range(n):
        if m[i] == '(':
            d += 1
        if m[i] == ')':
            d -= 1
            if d < -1:
                d -= 400001
    if d == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
