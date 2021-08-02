mi = lambda: [int(i) for i in input().split()]

n = int(input())
a = sorted(mi())
m = int(input())
q = mi()

s = sum(a)

for i in q:
    print(s - a[-i])
