n, k = list(map(int, input().split()))
s = input()
s += s


def judge(a, b):
    if (a == 'S' and b == 'R') or (a == 'R' and b == 'P') or (a == 'P' and b == 'S'):
        return b
    else:
        return a


hands = [''] * (2 * n)
for i in range(len(s)):
    hands[i] = s[i]

for i in range(k):
    for j in range(n):
        hands[j] = judge(hands[2 * j], hands[2 * j + 1])
    hands[n:] = hands[:n]

print((hands[0]))
