with open(0) as f:
    C = ''.join(f.read().split())
print('YES' if C == C[::-1] else 'NO')
