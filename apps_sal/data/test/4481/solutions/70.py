from collections import Counter

n = int(input())
S = [input() for _ in range(n)]
C = Counter(S)
C_most = C.most_common()

ans = []
for key, val in C_most:
    if val == C_most[0][1]:
        ans.append(key)
    else:
        break
        
print(*sorted(ans), sep='\n')
