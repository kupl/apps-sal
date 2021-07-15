n = int(input())
clients = []
for i in range(1, n + 1):
    clients.append(list(map(int, input().split())))
    clients[-1].reverse()
    clients[-1] += [i]
k = int(input())
r = list(map(int, input().split()))

s = 0
answer = []
clients.sort(reverse = True)
r = [1001] + r
for i in clients:
    pos = 0
    for j in range(k + 1):
        if r[j] >= i[1] and r[j] < r[pos]:
            pos = j
    if r[pos] >= i[1] and pos:
        answer.append(str(i[2]) + ' ' + str(pos))
        r[pos] = 0
        s += i[0]

print(len(answer), s)
print('\n'.join(answer))

