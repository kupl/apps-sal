n = int(input())
a = [int(input()) for i in range(n)]
b = sorted(a, reverse=True)
first, second = b[0], b[1]

for i in range(n):
    print(second if a[i] == first else first)
