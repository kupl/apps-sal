N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))

temp_diff = []
for i in range(N):
    temp_avr = T - H[i] * 0.006
    temp_diff.append(abs(A - temp_avr))

min_diff = min(temp_diff)
print(temp_diff.index(min_diff) + 1)
