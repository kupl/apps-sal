n = int(input())
a = [tuple(map(int, input().split())) for i in range(n)]
b = [tuple(map(int, input().split())) for i in range(n)]
a.sort()
b.sort(reverse=True)
print(a[0][0] + b[0][0], a[0][1] + b[0][1])
