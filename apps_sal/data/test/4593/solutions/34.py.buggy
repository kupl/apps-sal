x = int(input())
if x == 1000:
    print(1000)
    return
list_exp = []
max_b = int(1000 ** 0.5)
max_p = 0
while True:
    if 2 ** max_p > 1000:
        break
    else:
        max_p += 1

for b in range(1, max_b + 1):
    for p in range(2, max_p):
        if b ** p <= 1000:
            list_exp.append(b ** p)
        else:
            break
list_exp.sort()
for i in range(0, len(list_exp)):
    if list_exp[i] <= x:
        continue
    else:
        print(list_exp[i - 1])
        break
