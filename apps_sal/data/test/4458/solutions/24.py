n = int(input())
p = list(map(int, input().split()))
count = 0
a = p[0]
for x in range(len(p)):
    if p[x] <= a:
        count += 1
        a = p[x]
print(count)
