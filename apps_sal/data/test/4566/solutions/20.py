(N, M) = list(map(int, input().split()))
a_s = []
b_s = []
for i in range(M):
    (a, b) = list(map(int, input().split()))
    a_s.append(a)
    b_s.append(b)
for i in range(1, N + 1):
    print(a_s.count(i) + b_s.count(i))
