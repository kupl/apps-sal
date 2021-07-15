N = int(input())
A = list(map(int, input().split()))
result = "APPROVED"

for n in A:
    if n % 2 == 0:
        if not (n % 3 == 0 or n % 5 == 0):
            result = "DENIED"

print(result)
