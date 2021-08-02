n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = a.count(1)
c = min(b, n - b)
s = ''
for i in range(m):
    left, right = list(map(int, input().split()))
    length = right - left + 1
    if length % 2 or length // 2 > c:
        s += "0\n"
    else:
        s += "1\n"
print(s)
