s = input()
t = input()
s = sorted(s)
t = sorted(t, reverse=True)

print('Yes' if s < t else 'No')
