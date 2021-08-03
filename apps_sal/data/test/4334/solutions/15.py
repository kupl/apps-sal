S, T = input().split()
A, B = map(int, input().split())
U = input()

if U == S:
    A -= 1
elif U == T:
    B -= 1
print('{} {}'.format(A, B))
