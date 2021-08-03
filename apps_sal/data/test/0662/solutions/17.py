n = int(input())
c = 3
g = True
for i in range(n):
    t = int(input())
    if t == c:
        g = False
    else:
        c = list({1, 2, 3} ^ {t, c})[0]
if g:
    print("YES")
else:
    print("NO")
