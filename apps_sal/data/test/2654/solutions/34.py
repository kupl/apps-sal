N = int(input())
t = N // 2
la, lb = [], []
for _ in range(N):
    A, B = list(map(int, input().split()))
    la.append(A)
    lb.append(B)
la.sort()
lb.sort()
print((lb[t] - la[t] + 1 if N % 2 else lb[t - 1] - la[t] + lb[t] - la[t - 1] + 1))
