N, M = [int(x) for x in input().split()]
XYZ = [[int(x) for x in input().split()] for _ in range(N)]

ans = -float("inf")

for i in range(2 ** 3):
    hugo = [1, 1, 1]
    for j in range(3):
        if i >> j & 1 != 1:
            hugo[j] = -1

    A = []
    for x, y, z in XYZ:
        A.append(x * hugo[0] + y * hugo[1] + z * hugo[2])

    A.sort(reverse=True)
    ans = max(ans, sum(A[:M]))

print(ans)



