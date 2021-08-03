n = int(input())
a = list(map(int, input().split()))

n = len(set(a))
if n % 2 == 0:
    print(n - 1)
else:
    print(n)
