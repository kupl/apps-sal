n = int(input())
s = sorted([int(i) for i in input().split()])
need = 1
for i in s:
    if i >= need:
        need += 1
print(need - 1)
