s = input()
t = input()
n = len(s)
if t == s[:n] + t[-1]:
    print('Yes')
else:
    print('No')
