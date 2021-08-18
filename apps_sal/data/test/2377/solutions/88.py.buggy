import sys

input = sys.stdin.readline

N, H = map(int, input().split())
katanas = []
for _ in range(N):
    a, b = map(int, input().split())
    katanas.append((a, b))

max_a = sorted(katanas, reverse=True)[0][0]
throws = []
for a, b in katanas:
    if max_a < b:
        throws.append(b)

ans = 0
for b in sorted(throws, reverse=True):
    H -= b
    ans += 1
    if H <= 0:
        print(ans)
        return

print(ans + (H - 1) // max_a + 1)
