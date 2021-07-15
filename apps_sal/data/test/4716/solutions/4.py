n, k = map(int, input().split())
l = [int(s) for s in input().split()]

l.sort(reverse=True)
length = 0
for i in range(k):
    length += l[i]
print(length)
