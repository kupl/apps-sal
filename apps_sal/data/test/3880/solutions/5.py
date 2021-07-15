3

n = int(input())
data = list(map(int, input().split()))

negative, zero, positive = 0, 0, 0
for x in data:
    if x < 0:
        negative += 1
    elif x == 0:
        zero += 1
    else:
        positive += 1

seen = {}
min_negative = negative

def go(negative, positive):
    nonlocal n, min_negative
    if (negative, positive) in seen:
        return
    seen[(negative, positive)] = True
    min_negative = min(min_negative, negative)
    for i in range(min(n, negative)+1):
        for j in range(min(n-i, zero)+1):
            k = n - i - j
            if k <= positive:
                go(negative-i+k, positive-k+i)

go(negative, positive)

values = sorted(list(map(abs, data)))
for i in range(min_negative):
    values[i] *= -1

print(sum(values))


