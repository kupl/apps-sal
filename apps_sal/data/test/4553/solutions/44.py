(a, b) = list(map(int, input().split()))
s = input()
if s[:a].isdecimal() and s[a] == '-' and s[a + 1:].isdecimal():
    print('Yes')
else:
    print('No')
