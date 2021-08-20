n = int(input())
t = list(map(int, input().split()))
n = 2 * n
M = 2750131 + 10
d = [0] * M
nr = [0] * M
akt_nr = 1
for i in range(2, M):
    if d[i] == 0:
        d[i] = 1
        nr[i] = akt_nr
        akt_nr += 1
        for j in range(i * i, M, i):
            if d[j] == 0:
                d[j] = j // i
count = [0] * M
numbers = []
for x in t:
    if count[x] == 0:
        numbers.append(x)
    count[x] += 1
numbers.sort()
ans = []
for i in range(len(numbers) - 1, 0, -1):
    x = numbers[i]
    while count[x] > 0:
        count[x] -= 1
        if d[x] == 1:
            ans.append(nr[x])
            count[nr[x]] -= 1
        else:
            ans.append(x)
            count[d[x]] -= 1
print(*ans)
