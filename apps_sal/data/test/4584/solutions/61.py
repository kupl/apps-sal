n = int(input())
a = list(map(int, input().split()))
c = [0 for _ in range(n)]
for i in range(len(a)):
    c[a[i] - 1] += 1
for j in range(len(c)):
    print((c[j]))
