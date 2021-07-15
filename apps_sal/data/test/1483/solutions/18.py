N = int(input())
S = [int(x) for x in input().split(" ")]
lookup = {}

for i, v in enumerate(S):
    lookup[i+1] = v

for i in range(1, N + 1):
    visited = {}
    student = i

    while not (student in visited):
        visited[student] = True
        student = lookup[student]

    print(student, end=" ")

