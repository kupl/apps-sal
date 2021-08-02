
n = int(input())

ans = [[0, 0], [0, 1], [1, 0], [1, 1]]

p = 1

for i in range(n):

    p += 1
    ans.append([p, p])
    ans.append([p, p - 1])
    ans.append([p - 1, p])

print(len(ans))

for i in ans:

    print(*i)
