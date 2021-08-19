n = int(input())
A = [0]
a = list(map(int, input().split()))
for a_ in a:
    A.append(a_)
s = 0
A.append(0)
for i in range(n + 1):
    s += abs(A[i + 1] - A[i])
for i in range(1, n + 1):
    print(s + abs(A[i + 1] - A[i - 1]) - (abs(A[i + 1] - A[i]) + abs(A[i] - A[i - 1])))
