(N, A, B) = list(map(int, input().split()))
cnt = 0
for n in range(1, N + 1):
    val = n % 10
    tmp = n
    while tmp // 10 > 0:
        tmp = tmp // 10
        val += tmp % 10
    if val >= A and val <= B:
        cnt += n
print(cnt)
