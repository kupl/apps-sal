input()
l = list(map(int, input().split()))
while l and l[0] == 0:
    l = l[1:]
while l and l[-1] == 0:
    l = l[:-1]
for i in range(1, len(l) - 1):
    if l[i - 1] == 1 and l[i] == 0 and l[i + 1] == 1:
        l[i] = 1
print(l.count(1))
