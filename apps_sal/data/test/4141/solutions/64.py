n = int(input())
a = list(map(int, input().split()))
print('APPROVED' if all((a_ % 3 == 0 or a_ % 5 == 0 for a_ in a if a_ % 2 == 0)) else 'DENIED')
