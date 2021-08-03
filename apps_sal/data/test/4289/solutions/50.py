N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

min_value = abs(A - (T - H[0] * 0.006))
min_index = 1
for i in range(1, len(H)):
    if(min_value > abs(A - (T - H[i] * 0.006))):
        min_value = abs(A - (T - H[i] * 0.006))
        min_index = i + 1
print(min_index)
