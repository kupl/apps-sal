a = input()
b = input()
t = 0
ans = 0
p = len(b) - len(a) + 1

for i in range(len(b) - len(a) + 1):
    t += int(b[i])

for j in range(len(a)):
    v = int(a[j])
    if v == 1:
        ans = ans + p - t
    else:
        ans = ans + t
    if j == len(a) - 1:
        break
    t = t + int(b[p + j])
    t = t - int(b[j])

print(ans)
