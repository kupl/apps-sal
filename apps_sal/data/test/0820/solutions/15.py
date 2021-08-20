n = int(input())
m = int(input())
flashed = [int(input()) for i in range(n)]
flashed.sort(reverse=True)
(counter, sumSize) = (0, 0)
for size in flashed:
    sumSize += size
    counter += 1
    if sumSize >= m:
        break
print(counter)
