N, A, B = map(int, input().split())


def calc(N):
    sum = 0
    while N > 0:
        sum += N % 10
        N //= 10
    return sum


sum_num = 0
for i in range(1, N + 1):
    ans = calc(i)
    if A <= ans <= B:
        sum_num += i

print(sum_num)
