input()
a = sorted(map(int, input().split()))
while len(a) > 1:
    a.append((a.pop(0) + a.pop(0)) / 2)
    a.sort()
print(*a)
