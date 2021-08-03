n = list(map(int, input().split()))
s = 0
b = False
for i in range(6):
    s += n[i]
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            if n[i] + n[k] + n[j] == s // 2:
                b = True
if s % 2 == 1:
    b = False
if b:
    print("YES")
else:
    print('NO')
