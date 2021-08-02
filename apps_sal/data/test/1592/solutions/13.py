n = int(input())

message = 0
m = 0
l = 0

for _ in range(n):
    t, c = list(map(int, input().split()))
    message = max(0, message - (t - l))
    message += c
    m = max(message, m)
    l = t

print(l + message, m)
