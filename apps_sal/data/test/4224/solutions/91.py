n = int(input())
a = map(int, input().split())
c = 0
for i in a:
    while i % 2 == 0:
        i = i // 2
        c += 1
print(c)
