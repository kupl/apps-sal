N = int(input())
T, A = list(map(int, input().split()))
H = list(map(int, input().split()))

avg_tmp = []

for i in range(N):
    avg_tmp.append(T*1000 - (H[i] * 6))
abs_tmp = []
for j in range(N):
    abs_tmp.append(abs(A*1000 - avg_tmp[j]))

ans = abs_tmp.index(min(abs_tmp)) + 1

print(ans)

