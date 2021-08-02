n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

curl_ud_weights = [0] * n
curl_du_weights = [0] * n

sums = [0] * n

sums[n - 1] = a[n - 1] + b[n - 1]
curl_ud_weights[n - 1] = b[n - 1]
curl_du_weights[n - 1] = a[n - 1]

for i in range(n - 2, -1, -1):
    sums[i] = sums[i + 1] + (a[i] + b[i])
    remain = n * 2 - i * 2 - 1
    curl_ud_weights[i] = sums[i + 1] + curl_ud_weights[i + 1] + remain * b[i]
    curl_du_weights[i] = sums[i + 1] + curl_du_weights[i + 1] + remain * a[i]
    #print(sums[i] + curl_ud_weights[i + 1], remain, "*", b[i])

# -----------------------------------------------------

snake_weight = 0
max_weight = 0
current_weight = -1

for t in range(0, 2 * n, 2):
    remain = t % 4
    #print(t, snake_weight, a[t//2], b[t//2])
    if remain == 0:
        current_weight = sums[t // 2] * t + curl_ud_weights[t // 2] + snake_weight
        snake_weight += (a[t // 2] * t + b[t // 2] * (t + 1))
    elif remain == 2:
        current_weight = sums[t // 2] * t + curl_du_weights[t // 2] + snake_weight
        snake_weight += (b[t // 2] * t + a[t // 2] * (t + 1))

    if current_weight > max_weight:
        max_weight = current_weight
        #print(max_weight, t)

print(max_weight)
# print(curl_ud_weights)
# print(curl_du_weights)
# print(sums)

"""
3
0 1 0
0 0 0
"""
