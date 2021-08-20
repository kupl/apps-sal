import bisect
(n, m) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
answer = []
students = [0] * 100
for i in range(n):
    time = m - a[i]
    counter = 0
    for j in range(100):
        x = min(time // (j + 1), students[j])
        counter += x
        time -= x * (j + 1)
    answer.append(i - counter)
    students[a[i] - 1] += 1
print(*answer)
