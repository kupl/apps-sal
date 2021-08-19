s, c = list(map(int, input().split()))
i = min(s, c // 2)
m = i
s -= i
c -= i * 2
if s == 0:
    m += c // 4
# print(s,c)
print(m)
