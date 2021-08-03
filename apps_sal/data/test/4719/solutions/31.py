n = int(input())
li = []
for i in range(n):
    li.append(input())

for i in [chr(ord("a") + j) for j in range(26)]:
    print(i * min([li[k].count(i) for k in range(n)]), end="")

print("")
