N = int(input())
tasks = []
time = 0
ans = "Yes"
for _ in range(N):
    A, B = map(int, input().split())
    tasks.append((B, A))
tasks.sort()
for b, a in tasks:
    time += a
    if b < time:
        ans = "No"
        break
print(ans)
