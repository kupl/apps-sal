n = int(input())
L = list(map(int, input().split()))
L = [0] + L
num = 0
for i in range(n):
    if L[i] <= L[i + 1]:
        num += L[i + 1] - L[i]
print(num)
