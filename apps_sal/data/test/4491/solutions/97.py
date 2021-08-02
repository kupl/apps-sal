n = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
max_p = -1

for i in range(n):
    point = sum(A1[:i + 1]) + sum(A2[i:])
    max_p = max(max_p, point)
print(max_p)
