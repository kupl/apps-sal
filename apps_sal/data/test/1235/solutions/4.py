n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]
a.sort()
b.sort()
print(a[-1], b[-1])
