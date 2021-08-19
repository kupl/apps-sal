sux = 0
two = 0
x = int(input())
s = list(map(int, input().split(' ')))
t = [0] * 1000001
for i in s:
    t[i] += 1
for i in range(len(t) - 1, 0, -1):
    if t[i] % 2 == 1 and t[i - 1] > 0:
        t[i] -= 1
        t[i - 1] += 1
    elif t[i] % 2 == 1 and t[i] > 0:
        t[i] -= 1
for i in range(len(t) - 1, 0, -1):
    if two != 0 and t[i] != 0:
        sux += i * two
        two = 0
        t[i] -= 2
    if t[i] % 4 == 0:
        sux += t[i] // 4 * i * i
    else:
        sux += t[i] // 4 * i * i
        if two != 0:
            sux += i * two
            two = 0
        else:
            two = i
print(sux)
