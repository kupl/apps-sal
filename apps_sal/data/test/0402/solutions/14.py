def r():
    return list(map(int, input().split()))


n, k = r()
m = 240
count = 0
for i in range(1, n + 1):
    if 5 * i + k > m:
        break
    count += 1
    k += 5 * i
print(count)
