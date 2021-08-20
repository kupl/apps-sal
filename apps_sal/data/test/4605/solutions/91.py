(N, A, B) = list(map(int, input().split()))


def ten_sumfunc(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans


total = 0
for i in range(N + 1):
    sum1 = ten_sumfunc(i)
    if A <= sum1 and sum1 <= B:
        total += i
print(total)
