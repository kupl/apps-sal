(K, N) = map(int, input().split())
A_l = sorted(map(int, input().split()))
d_l = [K + A_l[0] - A_l[N - 1]]
for i in range(1, N):
    d_l.append(A_l[i] - A_l[i - 1])
print(K - max(d_l))
