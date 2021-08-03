n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

b = []
for i in range(n):
    b += [i + 1] * a[i]


for i in q:
    print(b[i - 1])
