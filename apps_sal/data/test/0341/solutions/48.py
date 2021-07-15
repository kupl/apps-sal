n, k = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

dict = {
    'r': 'p',
    's': 'r',
    'p': 's'
}

hand = []
for t in T:
    hand.append(dict[t])

for i in range(n - k):
    if hand[i] == hand[i + k]:
        hand[i + k] = 'x'

ans = 0
for t in hand:
    if t == 'r':
        ans += R
    elif t == 's':
        ans += S
    elif t == 'p':
        ans += P
print(ans)
