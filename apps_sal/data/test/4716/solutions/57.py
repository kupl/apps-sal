n, k = map(int, input().split())
l = [int(x) for x in input().split()]
l.sort(reverse=True)
print(sum(l[0:k]))
