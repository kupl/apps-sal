n, k = map(int, input().split())

result = 0
curVal = n
for i in range(k):
    if curVal <= 1:
        break
    result += 2 * curVal - 3
    curVal -= 2

print(result)
