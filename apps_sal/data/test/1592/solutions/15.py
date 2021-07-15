max_q = q = 0
t0 = 0

for _ in range(int(input())):
    t, c = map(int, input().split())
    q = max(0, t0-t+q) + c
    max_q = max(q, max_q)
    t0 = t

print(t+q, max_q)
