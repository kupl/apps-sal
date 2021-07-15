n = int(input())
for d in range(2, n):
    if n % d == 0:
        print(min(d, n // d), max(d, n // d), sep="")
        break
