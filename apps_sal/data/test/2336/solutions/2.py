n, k, q = list(map(int, input().split()))

MAX_TEMP = 200000 + 10
temps = [0 for x in range(MAX_TEMP)]

for i in range(n):
    l, r = list(map(int, input().split()))
    temps[l] += 1
    temps[r + 1] -= 1

sums = [0 for x in range(MAX_TEMP)]
count = 0
for i in range(1, MAX_TEMP):
    count += temps[i]
    if count >= k:
        sums[i] = 1
    sums[i] += sums[i - 1]

answers = []
for i in range(q):
    a, b = list(map(int, input().split()))
    answers.append(sums[b] - sums[a - 1])

for ans in answers:
    print(ans)

