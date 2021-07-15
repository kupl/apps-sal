x = list(map(int, input().split()))[1 : ]
s = 1
for i in range(10000000): s *= i
print(*sorted(x))

