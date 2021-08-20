n = int(input())
(a, b) = (0, 0)
for _ in range(n):
    (u, v) = list(map(int, input().split()))
    if u > v:
        a += 1
    elif u < v:
        b += 1
if a > b:
    print('Mishka')
elif a < b:
    print('Chris')
else:
    print('Friendship is magic!^^')
