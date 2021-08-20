lst = input().split()
N = int(lst[0])
M = int(lst[1])
students = []
checkpoints = []
for i in range(N):
    students.append(input().split())
for i in range(M):
    checkpoints.append(input().split())


def distance(P, Q):
    return abs(int(P[0]) - int(Q[0])) + abs(int(P[1]) - int(Q[1]))


for s in students:
    l1 = [10 ** 10]
    l2 = [0]
    for i in range(M):
        if distance(s, checkpoints[i]) < l1[-1]:
            l1.append(distance(s, checkpoints[i]))
            l2.append(i + 1)
    print(l2[-1])
