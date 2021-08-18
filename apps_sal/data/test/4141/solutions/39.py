
N = int(input())
A = list(map(int, input().split()))

for x in A:
    if x % 2 == 0:
        if not (x % 3 == 0 or x % 5 == 0):
            print('DENIED')
            break
else:
    print('APPROVED')
