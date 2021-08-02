N = input()
*A, = map(int, input().split())

a = float('inf')
for i in range(min(A), max(A) + 1): a = min(a, sum([(k - i)**2 for k in A]))
print(a)
