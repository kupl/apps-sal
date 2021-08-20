(a, b) = input().split()
dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
a = dict[a]
b = dict[b]
if a < b:
    ans = '<'
elif b < a:
    ans = '>'
else:
    ans = '='
print(ans)
