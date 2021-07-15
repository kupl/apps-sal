N = int(input())
a = int(input())
b = int(input())
c = int(input())

solution = 0

if a >= b - c:
    if N >= b:
        solution = (N - b) // (b - c) + 1

    solution += (N - solution * (b - c)) // a
else:
    solution = N // a

print(solution)
