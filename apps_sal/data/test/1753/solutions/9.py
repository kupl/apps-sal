n, m = list(map(int, input().split()))
a = {q: [] for q in range(1, n + 1)}
for q in range(m):
    x, y = list(map(int, input().split()))
    a[min(x, y)].append(max(y, x))
a = {q: sorted(a[q]) for q in range(1, n + 1)}
answer = [[] for q in range(1, n + 1)]
q2 = 1
for q in range(1, n + 1):
    for q1 in a[q]:
        answer[q1 - 1].append(q2)
        answer[q - 1].append(q2)
        q2 += 1
    answer[q - 1].append(q2)
    q2 += 1
for q in range(n):
    print(len(answer[q]))
    for q1 in answer[q]:
        print(q + 1, q1)
