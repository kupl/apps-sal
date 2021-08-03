n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))
t = input()


def score(hand):
    if hand == 's':
        return r
    if hand == 'p':
        return s
    if hand == 'r':
        return p


ans = 0
changed = [0] * n

for i in range(n):
    if i >= k and t[i] == t[i - k] and changed[i - k] == 0:
        changed[i] = 1
        continue
    ans += score(t[i])

print(ans)
