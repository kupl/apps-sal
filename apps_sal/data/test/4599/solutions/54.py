n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
A = sum(a[0::2])
B = sum(a[1::2])
print(A - B)
