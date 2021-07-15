T = int(input())
for i in range(T):
    n, k = list(map(int, input().split()))
    if k % 3 != 0:
        if n % 3 == 0:
            print("Bob")
        else:
            print("Alice")
    else:
        quotient = k + 1
        remainder = n % quotient
        if remainder % 3 == 0 and remainder != k:
            print("Bob")
        else:
            print("Alice")
