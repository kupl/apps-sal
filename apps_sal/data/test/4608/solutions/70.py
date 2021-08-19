N = int(input())
A = []
for i in range(N):
    A.append(int(input()) - 1)

#A.insert(0, 0)
ans = -1
push = 0

for i in range(N + 1):

    if A[push] == 1:
        ans = i + 1
        break

    else:
        push = A[push]

print(ans)
