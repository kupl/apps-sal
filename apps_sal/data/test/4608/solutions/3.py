N = int(input())
A = []
for i in range(N):
    A.append(int(input()) - 1)

ans = -1
push = 0
count = [False] * N

for i in range(N + 1):

    if A[push] == 1:
        ans = i + 1
        break

    elif count[push]:
        break

    else:
        count[push] = True
        push = A[push]


print(ans)
