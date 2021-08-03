N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
sum1 = 0
sum2 = 0
for num in range(N):
    if num % 2 == 0:
        sum1 += A[num]
    else:
        sum2 += A[num]
print(sum1 - sum2)
