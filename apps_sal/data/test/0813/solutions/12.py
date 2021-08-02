(n, a, b) = map(int, input().split())
s = ''
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(1, n + 1):
    if i in a:
        s += '1 '
    else:
        s += '2 '
print(s)
