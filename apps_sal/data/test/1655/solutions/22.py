n = int(input())
ppl_delta = [0] * n
for i, claw_len in enumerate(map(int, input().split())):
    ppl_delta[i] += 1
    if i - claw_len >= 0:
        ppl_delta[i - claw_len] -= 1

ans = 0
current = 0

for i in range(n - 1, -1, -1):
    # print(current, ans)
    if current == 0:
        ans += 1
    current += ppl_delta[i]

print(ans)
