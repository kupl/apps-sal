C = sorted(list(map(int, input().split())))
print(('Yes' if C[0] + C[3] == C[1] + C[2] or sum(C[:3]) == C[3] else 'No'))
