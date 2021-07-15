n = int(input())
anums = list(map(int, input().split()))

result = 'APPROVED'
for anum in anums:
    if (anum % 2 == 0) and not ((anum % 3 == 0) or (anum % 5 == 0)):
        result = 'DENIED'
        break

print(result)
