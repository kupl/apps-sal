x, k, d = map(int, input().split())
lists = []
x = abs(x)

step = int(x / d)

if step >= k:
    answer = x - k * d
elif step < k:
    k_left = k - int(step)
    if k_left % 2 == 0:
        answer = x % d
    if k_left % 2 == 1:
        answer = abs(x - step * d - d)

print(answer)
