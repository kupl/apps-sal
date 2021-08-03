S = input()
ans = 0
hand = ['g', 'p']


def do(s, t):
    if s == t:
        return 0
    elif s == 'g':
        return 1
    else:
        return -1


for i, s in enumerate(S):
    ans += do(s, hand[i % 2])

print(ans)
