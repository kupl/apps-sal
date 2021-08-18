k1, k2, k3 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))
n = k1 + k2 + k3
assign = [0] * n
for i in l1:
    assign[i - 1] = 1
for i in l2:
    assign[i - 1] = 2
for i in l3:
    assign[i - 1] = 3
ilenie3wprawo = [0] * n
ilenie1wlewo = [0] * n
ilenie1wlewo[n - 1] = k2 + k3
i = n - 1
ilenie3wprawo[n - 1] = (1 if assign[n - 1] != 3 else 0)
while i > 0:
    i -= 1
    ilenie3wprawo[i] = ilenie3wprawo[i + 1]
    ilenie1wlewo[i] = ilenie1wlewo[i + 1]
    if assign[i] != 3:
        ilenie3wprawo[i] += 1
    if assign[i + 1] != 1:
        ilenie1wlewo[i] -= 1
odp = [0] * (n + 1)
odp[n] = k2 + k3
i = n
while i > 1:
    i -= 1
    if assign[i] == 2:
        odp[i] = odp[i + 1] - 1
    if assign[i] == 1:
        odp[i] = odp[i + 1] + 1
    if assign[i] == 3:
        odp[i] = min(odp[i + 1], ilenie1wlewo[i - 1] + ilenie3wprawo[i])
if assign[0] == 2:
    odp[0] = odp[1] - 1
if assign[0] == 1:
    odp[0] = odp[1] + 1
if assign[0] == 3:
    odp[0] = min(odp[i + 1], ilenie3wprawo[0])
print(min(odp))
