import numpy


N = int(input().strip())

V_array = []
C_array = []

V_array = [int(x) for x in input().split()]
C_array = [int(x) for x in input().split()]

ans = 0
for j in range(N):
    ans += V_array[j] - C_array[j] if V_array[j] > C_array[j] else 0


print(ans)
