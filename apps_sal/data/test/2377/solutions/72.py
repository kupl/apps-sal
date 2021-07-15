import math

N, H = list(map(int, input().split()))
A = []
B = []
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

A.sort(reverse=True)
B.sort(reverse=True)

a_max = A[0]

ans = 0
bi = 0
while H > 0:
    if bi < N and a_max <= B[bi]:
        ans += 1
        H -= B[bi]
        bi += 1
    else:
        ans += math.ceil(H / a_max)
        break
print(ans)

