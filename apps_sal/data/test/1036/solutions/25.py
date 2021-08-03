n, k = map(int, input().split())
S = list(input())
hands = ["R", "P", "S"]
for i in range(len(S)):
    S[i] = hands.index(S[i])


def judge(a, b):
    a, b = max(a, b), min(a, b)
    if (a, b) == (2, 0):
        return b
    else:
        return a


for _ in range(k):
    S += S
    T = []
    for i in range(1, len(S), 2):
        T.append(judge(S[i - 1], S[i]))
    S = T
print(hands[T[0]])
