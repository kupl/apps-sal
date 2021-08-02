n = int(input())
a = []
for i in range(n):
    l, r = map(int, input().split())
    a += [(l, r)]
k = int(input())

count = 0
for l, r in a:
    if not r < k:
        count += 1
print(count)
