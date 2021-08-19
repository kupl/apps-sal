N = int(input())
sites = [list(map(int, input().split())) for _ in range(N)]


def getDistance(A, B):
    x = A[0] - B[0]
    y = A[1] - B[1]
    return (x ** 2 + y ** 2) ** 0.5


totalDistance = 0
for i in range(N):
    for j in range(N):
        if i != j:
            totalDistance += getDistance(sites[i], sites[j])
print(totalDistance / N)
