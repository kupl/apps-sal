n, m = map(int, input().split())

state = [False] * m
count = 0
for i in range(n):
    for lamp in tuple(map(int, input().split()))[1:]:
        if not state[lamp - 1]:
            state[lamp-1] = True
            count += 1

print("YES" if count == m else "NO")
