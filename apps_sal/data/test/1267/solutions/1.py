n = int(input())
a = set(list(map(int, input().split())))
t = 0
if 0 in a:
    t = 1
print(len(a) - t)

