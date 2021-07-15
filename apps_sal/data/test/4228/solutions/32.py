apple_num, taste = map(int, input().split())
total = 0
table = []
total_ans = 0
manual = 100000000
ans = 0
for i in range(apple_num):
    table.append(i+1)

for j in range(apple_num):
    table[j] = taste + j
    total += taste + j

for k in range(apple_num):
    if manual > abs(table[k]):
        manual = abs(table[k])
        ans = k
for l in range(apple_num):
    if l == ans:
        continue
    else:
        total_ans += table[l]
print(total_ans)
