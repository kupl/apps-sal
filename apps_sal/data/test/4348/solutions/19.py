n, k = map(int, input().split())
s = input().rstrip()
for i in range(ord('a'), ord('z') + 1):
    if k <= 0:
        break
    if s.count(chr(i)) < k:
        k -= s.count(chr(i))
        s = s.replace(chr(i), '')
    else:
        s = s.replace(chr(i), '', k)
        k = 0
print(s)
