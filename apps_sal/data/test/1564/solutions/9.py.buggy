n = int(input())
s = list(input())
t = list(input())
plat1 = []
plat2 = []
tot = []
for i in range(n):
    if (s[i] == 'a' and t[i] == 'b'):
        plat1.append(i + 1)
    elif s[i] == 'b' and t[i] == 'a':
        plat2.append(i + 1)
m = len(plat1)
k = len(plat2)
for i in range(1, m, 2):
    tot.append((plat1[i - 1], plat1[i]))
for i in range(1, k, 2):
    tot.append((plat2[i - 1], plat2[i]))
if m % 2 == 1 and k % 2 == 1:
    x, y = plat1[-1], plat2[-1]
    tot.append((x, x))
    tot.append((x, y))
elif m % 2 == 1 and k % 2 == 0 or m % 2 == 0 and k % 2 == 1:
    print(-1)
    return
print(len(tot))
for item in tot:
    print(*item)
