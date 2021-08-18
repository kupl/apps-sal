n = int(input())
a = list(input())
b = list(input())

cnt_a = 0
cnt_b = 0
for i in range(n):
    if a[i] != "?":
        a[i] = [ord(a[i]), i + 1]
    else:
        a[i] = [1000, i + 1]
        cnt_a += 1
    if b[i] != "?":
        b[i] = [ord(b[i]), i + 1]
    else:
        b[i] = [1000, i + 1]
        cnt_b += 1

a.sort()
b.sort()
ans = 0

j = 0
i = 0
used_a = [0] * n
used_b = [0] * n
ans_m = []
while i < n and j < n:
    if a[i][0] == b[j][0] and a[i][0] != 1000 and used_a[i] == 0 and used_b[j] == 0:
        ans_m.append([a[i][1], b[j][1]])
        used_a[i] = 1
        used_b[j] = 1
        ans += 1
        j += 1
        i += 1
    elif a[i][0] > b[j][0]:
        j += 1
    else:
        i += 1


print(min(n, ans + cnt_a + cnt_b))
for q in range(ans):
    print(ans_m[q][0], ans_m[q][1])
j = 0

for i in range(n):
    if a[i][0] == 1000 and used_a[i] == 0:
        while used_b[j] == 1 and j < n:
            j += 1
            if j == n:
                break
        if j == n:
            break
        if used_b[j] == 0 and used_a[i] == 0:
            print(a[i][1], b[j][1])
            used_a[i] = 1
            used_b[j] = 1

j = 0
for i in range(n):
    if b[i][0] == 1000 and used_b[i] == 0:
        while used_a[j] == 1 and j < n:
            j += 1
            if j == n:
                break
        if j == n:
            break
        if used_a[j] == 0 and used_b[i] == 0:
            print(a[j][1], b[i][1])
            used_a[j] = 1
            used_b[i] = 1
