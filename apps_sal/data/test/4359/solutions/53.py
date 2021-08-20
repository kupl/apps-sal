x = [int(input()) for i in range(5)]
tmp1 = []
for i in range(5):
    tmp2 = str(x[i])
    tmp1.append(int(tmp2[-1]))
for i in range(5):
    if tmp1[i] == 0:
        tmp1[i] = 10
m = tmp1.index(min(tmp1))
ans = 0
for i in range(5):
    if i == m:
        continue
    elif tmp1[i] == 10:
        ans += x[i]
    else:
        ans += x[i] + (10 - tmp1[i])
print(ans + x[m])
