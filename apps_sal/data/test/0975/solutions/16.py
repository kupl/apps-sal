n = int(input())
s = list(map(int, list(input())))
m = map(int, list(input()))

ma = [0] * 10
for dig in m:
    ma[dig] += 1

ma2 = list(ma)

min_f = 0
for nu in s:
    for x in range(nu, 10):
        if ma[x] > 0:
            ma[x] -= 1
            break
    else:
        min_f += 1
        for z in range(len(ma)):
            if ma[z] > 0:
                ma[z] -= 1
                break

print(min_f)

ma = ma2

max_f = 0
for nu in s:
    for x in range(nu + 1, 10):
        if ma[x] > 0:
            ma[x] -= 1
            max_f += 1
            break
    else:
        for z in range(len(ma)):
            if ma[z] > 0:
                ma[z] -= 1
                break

print(max_f)
