import sys
s = sys.stdin.readline().strip()
print('Yes' if any(x in s for x in ['ABC', 'ACB', 'BCA', 'BAC', 'CAB', 'CBA']) else 'No')
