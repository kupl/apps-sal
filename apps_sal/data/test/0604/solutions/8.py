n = int(input())
a = set(list(map(int, input().split())))
if 0 in a:
    a.remove(0)
print(len(a))
