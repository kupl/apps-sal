n, k = list(map(int, input().split()))

arr = sorted(list(map(int, input().split())))

median = arr[n // 2]

jumps = []

for i in range(n // 2 + 1, n):
    jumps.append(arr[i] - arr[i - 1])

for i in range(len(jumps)):
    weight = i + 1
    if weight * jumps[i] > k:  # the median cannot go jumps[i] jumps
        this_jump = k // weight
        median += this_jump
        k -= this_jump * weight
        break
    k -= weight * jumps[i]
    median += jumps[i]

weight = n // 2 + 1
median += k // weight

print(median)
