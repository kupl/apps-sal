N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
count = 0

for i in range(N - 2):
    if x[i] == y[i] and x[i + 1] == y[i + 1] and x[i + 2] == y[i + 2]:
        print("Yes")
        count = 1
        break

if count == 0:
    print("No")
