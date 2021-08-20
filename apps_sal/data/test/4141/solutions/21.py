N = int(input())
A = list(map(int, input().split()))
approved = all([a % 2 == 1 or a % 6 == 0 or a % 10 == 0 for a in A])
print('APPROVED' if approved else 'DENIED')
