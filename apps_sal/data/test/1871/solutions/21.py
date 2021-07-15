import sys

# f = open("b.txt", "r+")
f = sys.stdin

n, x = map(int, f.readline().strip().split())
c = list(map(int, f.readline().strip().split()))

c.sort()

time = 0

for i in c:
    time += i*x
    x -= 1 if x > 1 else 0

print(time)
