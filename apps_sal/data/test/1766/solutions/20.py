import sys
n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split(' ')]
sum = [0, 0]
start = 0
end = n - 1
i = 0
while start != end:
    if a[start] >= a[end]:
        sum[i] += a[start]
        start += 1
    else:
        sum[i] += a[end]
        end -= 1
    i = (i + 1) % 2
sum[i] += a[start]
print(sum[0], sum[1])
