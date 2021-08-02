N = int(input())
A = []
for i in range(N):
    A.append(int(input()) - 1)

ans = -1
push = 0
count = set()

for i in range(N + 1):

    if A[push] == 1:
        ans = i + 1
        break

    elif A[push] in count:
        break

    else:
        count.add(push)
        push = A[push]

print(ans)
