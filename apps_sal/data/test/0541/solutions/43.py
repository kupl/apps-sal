N, M = list(map(int, input().split()))

instructions = []
for _ in range(M):
    a = list(map(int, input().split()))
    instructions.append(a)
instructions.sort(key=lambda x:x[1])

ans = 0
current = 0
for a, b in instructions:
    if current < a: #過去の条件ではまだ満たしてない
        current = b-1
        ans += 1
print(ans)

