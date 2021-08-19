n = int(input())
a = sorted([[int(i) for i in input().split()] for j in range(n)])
b = sorted([[int(i) for i in input().split()] for j in range(n)], reverse=True)
print(a[0][0] + b[0][0], a[0][1] + b[0][1])
