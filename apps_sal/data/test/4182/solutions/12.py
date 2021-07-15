N,M,X,Y = map(int, input().split())
A = list(map(int, input().split())) + [X]
B = list(map(int, input().split())) + [Y]

print('No War' if max(A) < min(B) else 'War')
