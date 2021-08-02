n = int(input())
arr = list(map(int, input().split()))
sum = 0
for x in arr:
    sum += x
result = n - 1
if sum % n == 0:
    result = n
print(result)
