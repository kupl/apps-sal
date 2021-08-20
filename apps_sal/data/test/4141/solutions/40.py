n = int(input())
a = list(map(int, input().split()))
z = 1
for i in a:
    if i % 2 == 0:
        if not (i % 3 == 0 or i % 5 == 0):
            z = 0
            break
print('APPROVED' if z == 1 else 'DENIED')
