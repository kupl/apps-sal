n = int(input())
mountains = list(map(int, input().split()))
total = 0
mountains_current = []
for i in range(n):
    mountains_current.append(mountains[i])
    if mountains[i] >= max(mountains_current):
        total += 1
print(total)
