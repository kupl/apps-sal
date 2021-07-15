a, b = map(int, input().split())
s = input()
t = s.split('-')
print('Yes' if s[a] == '-' and len(t) == 2 else 'No')
