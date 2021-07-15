n, m = map(int, input().split())
answer = 0
for i in range(1, n + 1):
    if m % i == 0 and m // i <= n:
        answer += 1
print(answer)
