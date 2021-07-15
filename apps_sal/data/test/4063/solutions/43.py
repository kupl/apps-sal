N = int(input())
d = [int(c) for c in input().split()]
d.sort()
print(d[int(N/2)]-d[int(N/2)-1])
