def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


N = int(input())
A = list(map(int, input().split()))
answer = A[0]
for a in A:
    answer = gcd(answer, a)
print(answer)
