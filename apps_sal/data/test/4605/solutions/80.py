(N, A, B) = map(int, input().split())
sum1 = 0
for n in range(1, N + 1):
    sum2 = 0
    for s in str(n):
        sum2 += int(s)
    if A <= sum2 <= B:
        sum1 += n
print(sum1)
