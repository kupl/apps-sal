n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(a)
for i in a:
    print(b[-1] if i != b[-1] else b[-2])
