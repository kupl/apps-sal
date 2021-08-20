maxx = 0
for i in range(int(input())):
    (a, b) = map(int, input().split())
    maxx = max(a + b, maxx)
print(maxx)
