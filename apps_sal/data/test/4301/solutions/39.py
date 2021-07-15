n = int(input())
a = [int(input()) for _ in range(n)]
s = sorted(a)
for i in range(n):
    if a[i] != s[-1]:
        print(s[-1])
    else:
        print(s[-2])
