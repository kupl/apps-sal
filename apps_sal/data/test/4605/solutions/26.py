N, A, B = map(int, input().split())

ans = 0

for i in range(1, N + 1):

    x = str(i)
    n = len(x)
    sum = 0

    for j in range(0, n):
        sum = sum + int(x[j])

    if sum >= A and sum <= B:
        ans += i

print(ans)
