n = int(input())

a = list(map(int, input().split()))

result = 0

for i in a:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            result = 'APPROVED'
        else:
            result = 'DENIED'
            break
    else:
        result = 'APPROVED'
print(result)
