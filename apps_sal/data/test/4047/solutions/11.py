n = int(input())
odd = sum((e & 1 for e in map(int, input().split())))
print(min(odd, n - odd))
