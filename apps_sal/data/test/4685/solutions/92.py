l = list(map(int, input().split()))
k = int(input())
l.sort()
print(l[0] + l[1] + l[2] * 2 ** k)
