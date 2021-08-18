N = int(input())
a = list(map(lambda x: int(x), input().split(" ")))
sums = [0] * (10**5 + 1)

for val in a:
    if val - 1 >= 0:
        sums[val - 1] = sums[val - 1] + 1
    sums[val] = sums[val] + 1
    if val + 1 <= 10**5:
        sums[val + 1] = sums[val + 1] + 1

print(max(sums))
