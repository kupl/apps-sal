n, c = list(map(int, input().split()))

D_list = [[int(i) for i in input().split()] for _ in range(c)]
c_list = [[int(i) for i in input().split()] for _ in range(n)]

c_num = [[0 for _ in range(3)] for __ in range(c)]

for a in range(n):
    for b in range(n):
        c_num[c_list[b][a] - 1][(a + b + 2) % 3] += 1


ans = 10 ** 10
for i in range(1, c**3):
    x = i % c
    y = (i % c**2) // c
    z = i // c**2
    if x == y or y == z or z == x:
        continue
    else:
        color = [x, y, z]
        count = 0
        for s in range(3):
            for t in range(c):
                count += c_num[t][s] * D_list[t][color[s]]

        if count < ans:
            ans = count

print(ans)
