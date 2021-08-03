a, b = map(int, input().split())
le = list(map(int, input().split()))
le.sort()
gou = 0
for i in range(b):
    gou += le.pop()
print(gou)
