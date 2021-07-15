n = int(input())

def yakusu(x):
    xx = 2
    y = []
    while xx**2 < x:
        if x%xx == 0:
            y.append(xx)
            y.append(x//xx)
        xx += 1
    if xx**2 == x:
        y.append(xx)
    y.append(x)
    return y
    
if n == 2:
    ans = 0
else:
    ans = len(yakusu(n-1))

for i in yakusu(n):
    nn = n
    while True:
        if nn%i == 0:
            nn = nn//i
        else:
            break
    if nn%i == 1:
        ans += 1

print(ans)

