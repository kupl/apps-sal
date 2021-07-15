N = int(input())
K = int(input())
init = 1
for i in range(N):
    init = min(init*2, init + K)
print(init)
