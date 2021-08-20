n = int(input())
A = 0
B = 0
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a > b:
        A += 1
    elif a < b:
        B += 1
if A > B:
    print('Mishka')
elif A < B:
    print('Chris')
else:
    print('Friendship is magic!^^')
