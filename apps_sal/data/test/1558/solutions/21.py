(n, r, avg) = list(map(int, input().split(' ')))
exams = [list(map(int, input().split(' '))) for _ in range(n)]
exams.sort(key=lambda x: x[1])
total = n * avg
cur = sum((e[0] for e in exams))
essays = 0
for e in exams:
    if cur >= total:
        break
    its = min(r - e[0], total - cur)
    cur += its
    e[0] += its
    essays += its * e[1]
print(essays)
