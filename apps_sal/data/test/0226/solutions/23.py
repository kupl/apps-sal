n = int(input())
pieces = list(map(int, input().split()))
reversed_pieces = list(reversed(pieces))
TOTAL = []
current_total = 0
for piece in reversed_pieces:
    current_total += piece
    TOTAL.append(current_total)
HAS_TOKEN = 0
NO_TOKEN = 1
dp_alice = [[0] * n, [0] * n]
dp_bob = [[0] * n, [0] * n]
dp_alice[HAS_TOKEN][0] = dp_bob[HAS_TOKEN][0] = reversed_pieces[0]
dp_alice[NO_TOKEN][0] = dp_bob[NO_TOKEN][0] = 0
for i in range(1, n):
    dp_alice[HAS_TOKEN][i] = max(dp_alice[HAS_TOKEN][i - 1], dp_alice[NO_TOKEN][i - 1] + reversed_pieces[i])
    dp_bob[HAS_TOKEN][i] = max(dp_bob[HAS_TOKEN][i - 1], dp_bob[NO_TOKEN][i - 1] + reversed_pieces[i])
    dp_alice[NO_TOKEN][i] = TOTAL[i] - dp_bob[HAS_TOKEN][i]
    dp_bob[NO_TOKEN][i] = TOTAL[i] - dp_alice[HAS_TOKEN][i]
print(dp_alice[NO_TOKEN][-1], dp_bob[HAS_TOKEN][-1])
