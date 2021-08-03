n = int(input())
a = list(map(int, input().split()))
x = len([q for q in a if q % 2 == 0])
print(min(x, n - x))
