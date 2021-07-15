t = int(input())
r = 0
s = [0] * 10**5
ss = 0
for _ in range(t):
    x = input().split()
    if x[0] == 'add':
        r += 1
    elif x[0] == 'for':
        s[ss] = (r, int(x[1]))
        ss += 1
        r = 0
    elif x[0] == 'end':
        ss -= 1
        r_old, k = s[ss]
        r = r_old + r * k
        if r >= 2**32:
            print("OVERFLOW!!!")
            break
else:
    print(r if r < 2**32 else "OVERFLOW!!!")
