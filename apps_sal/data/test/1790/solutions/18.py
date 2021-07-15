n = int(input())
A = {}
B = {}
for i in range(n):
    if A:
        B = set(list(map(int, input().split()))[1:])
        A &= B
    else:
        A = set(list(map(int, input().split()))[1:])
print(' '.join(map(str, A)))
