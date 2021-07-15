n = int(input())
l = [*map(int, input().split())]
m = int(input())
l.sort()
s = sum(l)
for c in map(int, input().split()):
    print(s - l[-c])
