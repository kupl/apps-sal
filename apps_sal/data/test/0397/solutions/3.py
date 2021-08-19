(n, k) = map(int, input().split())
current = 1
actions = 1
step = 2
while n != actions + (current - k):
    current += step
    step += 1
    actions += 1
print(current - k)
