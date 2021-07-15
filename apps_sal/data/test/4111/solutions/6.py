n = int(input().strip())
weights = list(map(int, input().strip().split()))

res = 0

sum_even = sum(weights[1::2])
sum_odd = sum(weights[2::2])

for idx in range(n):
    if sum_even == sum_odd:
        res += 1
    if idx == n-1:
        break
    if idx % 2 == 0:
        sum_even += weights[idx]
        sum_even -= weights[idx+1]
    else:
        sum_odd += weights[idx]
        sum_odd -= weights[idx+1]

print(res)

