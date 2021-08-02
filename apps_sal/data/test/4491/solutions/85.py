N = int(input())

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ans = 0
for i in range(N):
    temp = sum(A1[:i + 1]) + sum(A2[i:])
    if temp > ans:
        ans = temp

print(ans)
