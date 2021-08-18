N = int(input())
a = list(map(int, input().split(" ")))
sums = [0] * (10**5)

for val in a:
    if val - 1 >= 0:
        sums[val - 1] = sums[val - 1] + 1
    sums[val] = sums[val] + 1
    if val + 1 < 10**5:
        sums[val + 1] = sums[val + 1] + 1

print(max(sums))
