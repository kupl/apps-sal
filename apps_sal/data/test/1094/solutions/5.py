A = []
for i in range(int(input())):
    A.append(input().strip())
names = set()
for i in range(len(A) - 1, -1, -1):
    if not A[i] in names:
        names.add(A[i])
        print(A[i])
