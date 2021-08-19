import sys

f = sys.stdin
# f = open("input.txt", "r")

x, k = map(int, f.readline().strip().split())

a = []

for i in range(k):
    a += list(map(int, f.readline().strip().split()))[1:]

a.sort()

sub = list(set(range(1, x)) - set(a))

max = len(sub)

i = 0

sync = 0
while i < len(sub) - 1:
    if sub[i + 1] - sub[i] == 1:
        i += 1
        sync += 1
    i += 1

min = max - sync

print(min, max)
