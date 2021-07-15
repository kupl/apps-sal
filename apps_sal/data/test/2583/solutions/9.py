from sys import stdin

def isPrime(n):
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    if n == 1:
        print("FastestFinger")
    elif n == 2:
        print("Ashishgup")
    elif n % 2 == 1:
        print("Ashishgup")
    elif n & (n-1) == 0:
        print("FastestFinger")
    elif (n/2) % 2 == 1 and isPrime(n/2):
        print("FastestFinger")
    else:
        print("Ashishgup")

