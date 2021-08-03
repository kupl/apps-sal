li = list(map(int, input().split()))

li.sort()

n = (li[1] - li[0]) + (li[2] - li[1])
print(n)
