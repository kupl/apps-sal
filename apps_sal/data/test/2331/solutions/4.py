def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if gcd(a, b) == 1:
        print("Finite")
    else:
        print("Infinite")

