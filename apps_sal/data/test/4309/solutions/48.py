N = int(input())

for i in range(N, 1000):
    i = str(i)
    if i[0] == i[1] and i[1] == i[2] and i[2] == i[0]:
        ans = i
        break

print(i)
