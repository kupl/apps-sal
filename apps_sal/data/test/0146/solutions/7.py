n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
answer = 0
for i in range(k):
    B = A.copy()
    C = []
    for j in range(n):
        if j % k != i:
            C.append(B[j])
    a = C.count(1)
    b = C.count(-1)
    if abs(a - b) > answer:
        answer = abs(a - b)
print(answer)

