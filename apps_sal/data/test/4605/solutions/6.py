N, A, B = map(int, input().split())

def caluculate(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

ans = 0
for i in range(N+1):
    if A <= caluculate(i) <= B:
        ans += i

print(ans)
