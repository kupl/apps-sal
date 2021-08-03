n = int(input())
size = int(input())
ary = [int(input()) for _ in range(n)]

ary.sort()
ary.reverse()

count = 0
while size > 0:
    count += 1
    size -= ary[count - 1]

print(count)
