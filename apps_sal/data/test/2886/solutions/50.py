from collections import defaultdict
S = input()


def unbalance(S):
    D = defaultdict(lambda: 0)
    for s in S:
        D[s] += 1
    if max(D.values()) > len(S) // 2:
        return True
    else:
        return False


lenS = len(S)
for i in range(lenS - 1):
    if unbalance(S[i:i + 2]):
        print(f'{i+1} {i+2}'); break
    if i < lenS - 2 and unbalance(S[i:i + 3]):
        print(f'{i+1} {i+3}'); break
else:
    print('-1 -1')
