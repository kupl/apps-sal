l = list(map(int, input().split()))
k = int(input())
l.sort()
print(l[2] * (2**k) + l[0] + l[1])
