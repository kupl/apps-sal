(a, b) = map(int, input().split())
s = [1, 3, 5, 7, 8, 10, 12]
t = [4, 6, 9, 11]
if a in s:
    a = 0
elif a in t:
    a = 1
else:
    a = 2
if b in s:
    b = 0
elif b in t:
    b = 1
else:
    b = 2
print('Yes' if a == b else 'No')
