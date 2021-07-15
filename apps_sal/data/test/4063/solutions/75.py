n = int(input())
d = list(map(int, input().split()))
d.sort()

half = n//2
first = d[half - 1]
second = d[half]

print(second - first)
