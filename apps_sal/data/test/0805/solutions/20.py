a = list()
n = int(input())
c = [1] * 100
(l, r) = map(int, input().split())
for i in range(n - 1):
    b = list(map(int, input().split()))
    for j in range(b[0], b[1]):
        c[j] = 0
print(sum(c[l:r]))
