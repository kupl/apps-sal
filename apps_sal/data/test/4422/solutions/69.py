(n, k) = map(int, input().split())
s = input()
result_s = ''
a = 0
for s in list(s):
    a += 1
    if a == k:
        s = s.lower()
    result_s += s
print(result_s)
