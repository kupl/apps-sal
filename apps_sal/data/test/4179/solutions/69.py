n, m, c = map(int, input().split())
b = list(map(int, input().split()))
answer = 0
memo = 0
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        memo += a[j] * b[j]
    memo += c
    if(memo > 0):
        answer += 1
    memo = 0
print(answer)
