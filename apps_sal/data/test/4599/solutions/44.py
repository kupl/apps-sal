n = int(input())
a = sorted(list(map(int, input().split())),reverse = True)
Alice = 0
Bob = 0
count = 0

while True:
    Alice += a[count]
    count += 1
    if count == n:
        print(Alice - Bob)
        return
    Bob += a[count]
    count += 1
    if count == n:
        print(Alice - Bob)
        return
