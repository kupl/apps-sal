n, r, avg = list(map(int, input().split()))
total = 0
exams = []
for i in range(n):
    score, cost = list(map(int, input().split()))
    total += score
    exams.append((cost, score))
need = n * avg - total
result = 0
exams.sort()
for cost, score in exams:
    if need <= 0:
        break
    x = min(need, r - score)
    result += cost * x
    need -= x
print(result)
