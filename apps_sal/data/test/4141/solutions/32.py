import sys

N = int(input())
A = list(map(int, input().split()))

for num in A:
    if num % 2 == 0:
        if not (num % 3 == 0 or num % 5 == 0):
            print("DENIED")
            return

print("APPROVED")
