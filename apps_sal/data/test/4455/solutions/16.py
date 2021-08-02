n, k = list(map(int, input().split()))
skills = list((list(map(int, input().split()))))
quarrels = [0] * n

for _ in range(k):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1

    if skills[x] > skills[y]:
        quarrels[x] += 1
    elif skills[y] > skills[x]:
        quarrels[y] += 1

result = [0] * n
next_p = 1

skills = sorted(enumerate(skills), key=lambda x: -x[1])

for i, skill in skills[:-1]:
    while next_p < n and skills[next_p][1] == skill:
        next_p += 1

    result[i] = n - next_p - quarrels[i]

print(' '.join(map(str, result)))
