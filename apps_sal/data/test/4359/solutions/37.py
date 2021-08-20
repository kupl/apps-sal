foods = [int(input()) for i in range(5)]
loss = [0] * 5
for i in range(5):
    if int(str(foods[i])[-1]) % 10 == 0:
        loss[i] = 0
    else:
        loss[i] = abs(10 - int(str(foods[i])[-1]))
lind = loss.index(max(loss))
lmax = foods[lind]
del foods[lind], loss[lind]
foods = [foods[i] + loss[i] for i in range(4)]
print(sum(foods) + lmax)
