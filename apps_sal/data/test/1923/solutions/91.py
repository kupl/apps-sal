n = int(input())
l = list(map(int, input().split()))
l.sort()
print(sum(l[0::2]))
