import sys

N, A, B = list(map(int, input().split()))

if A + B - 1 > N or A * B < N:
    print((-1))
    return

ans = []

for i in range(N - A + 1, N + 1, 1):
    ans.append(i)

now = []
for i in range(1, N - A + 1, 1):

    now.append(i)

    if len(now) == B - 1:
        now.reverse()

        for j in now:
            ans.append(j)
        now = []

now.reverse()
for j in now:
    ans.append(j)

print((" ".join(map(str, ans))))
