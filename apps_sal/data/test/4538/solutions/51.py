(N, D) = map(int, input().split())
zahyo = [list(map(int, input().split())) for i in range(N)]


def distance(a, b):
    return (a ** 2 + b ** 2) ** 0.5


kazu = 0
for i in range(N):
    genzai = zahyo[i]
    if distance(genzai[0], genzai[1]) <= D:
        kazu += 1
print(kazu)
