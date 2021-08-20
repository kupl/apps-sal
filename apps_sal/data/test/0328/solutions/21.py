n = int(input())
highest = 0
for i in range(n):
    (a, b) = map(int, input().split())
    if a + b > highest:
        highest = a + b
print(highest)
