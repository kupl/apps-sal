import sys
fin = sys.stdin

n = int(fin.readline())

count = 0
while n > 0:
    count += 1
    n -= max(map(int, str(n)))

print(count)
