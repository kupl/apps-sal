N = int(input())
A = list(map(int, input().split()))

p = []
for i in range(1, N + 1):
    p.append(i)

for i in range(N):
    if p[i] == A[i]:
        print((-1))
        return

index = 0
ans = []
for i in range(N):
    if A[i] == index + 1:
        for j in range(i - 1, index - 1, -1):
            A[j], A[j + 1] = A[j + 1], A[j]
            ans.append(j + 1)
        index = i

for i in range(len(A)):
    if i == len(A) - 1:
        break
    if A[i] + 1 == A[i + 1]:
        continue
    else:
        print((-1))
        return

for i in ans:
    print(i)

