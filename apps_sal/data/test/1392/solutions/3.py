n, k = list(map(int, input().split()))
b = {str(i) for i in range(k + 1)}
cnt = 0
for i in range(n):
    a = set(input())
    if a >= b:
        cnt += 1

print(cnt)
