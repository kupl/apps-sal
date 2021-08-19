inp = input()
n = int(inp)
c = 0
k = 10
while k ** c < n:
    c += 1
res = 0
res += 2 ** c - 2
p = 1
for i in range(len(inp) - 1, -1, -1):
    ch = inp[i]
    if ch == '7':
        res += p
    p *= 2
res += 1
print(res)
