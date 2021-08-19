(a, b) = map(str, input().split())
a = int(a)
li_b = []
for i in range(4):
    B = b[i]
    if B != '.':
        li_b.append(int(B))
b = 100 * li_b[0] + 10 * li_b[1] + li_b[2]
ans = a * b // 100
print(ans)
