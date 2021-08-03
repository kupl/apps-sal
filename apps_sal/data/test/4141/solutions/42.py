N = int(input())
A = list(map(int, input().split()))

result = 'DENIED'
for i in A:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            result = 'APPROVED'
        else:
            result = 'DENIED'
            break
    else:
        result = 'APPROVED'

print(result)
