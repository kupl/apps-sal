N = int(input())
B = tuple(map(int, input().split()))
result = B[0] + B[-1]
for i in range(N - 2):
    result += min(B[i], B[i + 1])
print(result)
