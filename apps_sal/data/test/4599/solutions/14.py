N = int(input())
A = list(map(int, input().split()))
A.sort()
Alice = 0
Bob = 0
while 1:
    try:
        Alice += A.pop(-1)
    except IndexError:
        break
    try:
        Bob += A.pop(-1)
    except IndexError:
        break
print(Alice - Bob)
