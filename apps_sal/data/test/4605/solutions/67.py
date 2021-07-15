N, A, B = map(int, input().split())

result = 0
for i in range(1, N+1):
    num = i//(10**4) + i//(10**3)%10 + i//(10**2)%10 + i//10%10 + i%10
    if A <= num <= B:
        result += i
print(result)
