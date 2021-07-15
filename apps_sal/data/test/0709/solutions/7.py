n = int(input())
#a = [int(c) for c in input().split()]
count = 0

while n > 0:
    if n & 1 == 1:
        count += 1
    n = n >> 1
print(count)

