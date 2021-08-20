from sys import stdin, stdout
(a, b) = list(map(int, stdin.readline().rstrip().split()))
years = 0
while a <= b:
    a *= 3
    b *= 2
    years += 1
print(years)
