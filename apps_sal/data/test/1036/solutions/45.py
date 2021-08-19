(N, K) = map(int, input().split())
S = list(input())
hand = ['R', 'P', 'S']
for i in range(N):
    S[i] = hand.index(S[i])


def judge(A, B):
    (A, B) = (min(A, B), max(A, B))
    if A == 0 and B == 2:
        return A
    else:
        return B


cnt = K
while cnt:
    S += S
    T = []
    for i in range(0, len(S), 2):
        T.append(judge(S[i], S[i + 1]))
    S = T
    cnt -= 1
print(hand[S[0]])
