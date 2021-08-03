n, k = map(int, input().split())
s = input()
min_c = n * 2
for i in range(k):
    c = chr(ord('A') + i)
    min_c = min(min_c, s.count(c))
print(min_c * k)
