#n = int(input())
#a, b = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]

a, b = list(map(str, input().split()))

a = int(a)
b = int(b[0] + b[2:])
print((a * b // 100))
