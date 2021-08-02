N = int(input())

i = int(N**0.5)

while N % i:
    i -= 1

print(i + N // i - 2)
