n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
lst = []
for i in range(m):
    a, b = list(map(int, input().split()))
    lst.append([a, b])
answer = 0
answer_1 = []
for i in range(n):
    B = A.copy()
    kek = []
    for j in range(m):
        a, b = lst[j][0], lst[j][1]
        if a <= i + 1 <= b:
            kek.append(j + 1)
            for q in range(a - 1, b):
                B[q] -= 1
    elem = max(B)
    if answer < elem - B[i]:
        answer = elem - B[i]
        answer_1 = kek.copy()
print(answer)
print(len(answer_1))
print(' '.join(map(str, answer_1)))
