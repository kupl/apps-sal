N = int(input())
C = [list(map(int,input().split())) for _ in range(N-1)]

for i in range(N-1):
    now = 0
    for j in range(i,N-1):
        now = max(C[j][1], -(-now//C[j][2])*C[j][2])
        now += C[j][0]
    print(now)
print(0)
