N = int(input())
K = int(input())
dist = 0
for val in list(map(int, input().split())):
    dist += 2 * min(val, abs(val - K))
print(dist)
