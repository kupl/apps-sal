n = int(input())
T = input()

b = 10**10
D = {'0': b, '1': b * 2, '11': b, '10': b, '01': b - 1, '00': 0}
if n < 3:
    print((D[T]))
    return

P = ["110", "101", "011"]
h, t = -1, -1
for i in range(3):
    if T[:3] == P[i]:
        h = 3 - i
    if T[-3:] == P[i]:
        t = i

a = 0
if t != -1 and h != -1 and (n - h - t) % 3 == 0:
    for i in range((n - h - t) // 3):
        if T[h + 3 * i:h + 3 * -~i] != P[0]:
            break
    else:
        a = 10**10 + 1 - (1 if t else 0) - (1 if h else 0) - (n - h - t) // 3

print(a)
