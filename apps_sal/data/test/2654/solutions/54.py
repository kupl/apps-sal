N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

# N = 3
# A = [[1, 3], [2, 5], [1, 7]]

if N % 2 == 1:
    minA = sorted([row[0] for row in A])
    maxA = sorted([row[1] for row in A])
    medA = minA[int(N / 2)]
    medB = maxA[int(N / 2)]
    print(medB - medA + 1)
else:
    minA = sorted([row[0] for row in A])
    maxA = sorted([row[1] for row in A])
    medA = (minA[int(N / 2 - 1)] + minA[int(N / 2)]) / 2
    medB = (maxA[int(N / 2 - 1)] + maxA[int(N / 2)]) / 2
    print(int((medB - medA) * 2 + 1))
