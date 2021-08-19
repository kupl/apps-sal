N = int(input())
A = list(map(int, input().split()))
if (N - len(set(A))) % 2 == 0:
    print(len(set(A)))
else:
    print(len(set(A)) - 1)
