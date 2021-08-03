N = int(input())
block = list(map(int, input().split()))
a = 1
for i in block:
    if i == a:
        a += 1
if a == 1:
    print(-1)
else:
    print(len(block) - a + 1)
