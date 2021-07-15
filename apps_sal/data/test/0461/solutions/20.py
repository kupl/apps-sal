n = int(input()) - 1
a = int(input())
b = int(input())
c = int(input())
print(max(min(n * a, n * b, (n - 1) * c + min(a, b)), 0))

