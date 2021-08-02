n = int(input())

p = list(map(int, input().split()))

ideal = list(range(1, n + 1))

count = 0
for x in range(n):
    if p[x] != ideal[x]:
        count += 1

if count == 0 or count == 2:
    print("YES")

else:
    print("NO")
