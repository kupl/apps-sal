a, b, c = map(int, input().split())
k = int(input())
l = [a, b, c]
l.sort()
print(l[-1] * 2**k + sum(l[:-1]))
