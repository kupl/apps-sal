N = int(input())
t = [0] * N
for i in range(N):
    t[i] = list(map(int, input().split()))

t = sorted(t, key = lambda x: x[1])

n = 0
d = 0
f = 0
for i in range(N):
    n += t[i][0]
    if n > t[i][1]:
        f = 1
        break

if f == 0:
    print("Yes")
else:
    print("No")
