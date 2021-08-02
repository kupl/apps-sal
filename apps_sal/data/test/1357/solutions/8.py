import sys
f = sys.stdin
#f = open("input.txt", "r")
n, m = map(int, f.readline().strip().split())
p = [int(i) for i in f.readline().strip().split()]
prev = 1
count = 0
for i in p:
    if i > prev:
        count += i - prev
    elif i < prev:
        count += n + i - prev
    prev = i
print(count)
