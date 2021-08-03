from collections import Counter
nl = Counter(input())
print('YES' if len(nl) == 1 or nl['-'] % nl['o'] == 0 else 'NO')
