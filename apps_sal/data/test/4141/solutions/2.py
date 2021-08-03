N = int(input())
A = list(map(int, input().split()))

result = "APPROVED"
for i in A:
    if (i % 2 == 0) and not((i % 3 == 0) or (i % 5 == 0)):
        result = "DENIED"
        break
print(result)
