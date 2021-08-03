N = int(input())

a = [list(map(int, input().split())) for _ in range(N)]

a = sorted(a, key=lambda x: x[1])

hours = 0

ans = "Yes"
for pair in a:
    hours += pair[0]
    deadline = pair[1]

    if hours > deadline:
        ans = "No"
        break

print(ans)
