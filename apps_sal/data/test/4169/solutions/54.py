(N, M) = map(int, input().split())
(A, B) = ({}, [])
for i in range(N):
    (a, b) = map(int, input().split())
    A[i] = a
    B.append(b)
A = sorted(A.items(), key=lambda x: x[1])
ans = 0
num = 0
for i in range(N):
    flag = False
    max_num = B[A[i][0]]
    for j in range(max_num):
        ans += A[i][1]
        num += 1
        if num == M:
            flag = True
            break
    if flag:
        break
print(ans)
