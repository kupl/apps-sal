a = input()

ans = 1

LIM = 100000 + 12
run = [0 for i in range(LIM)]

for i in range(1, LIM, 2):
    run[i] = 1

run[0] = 1
run[2] = 2
for i in range(4, LIM, 2):
    run[i] = run[i - 2] + run[i - 3]

lst = 0
for i in range(1, len(a)):
    sm = int(a[i]) + int(a[i - 1])
    if sm != 9:
        ans *= run[lst]
        lst = 0
    else:
        lst += 1

ans *= run[lst]

print(ans)

