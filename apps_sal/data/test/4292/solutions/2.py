a = list(map(int, input().split()))
N = a[0]
K = a[1]
p = list(map(int, input().split()))
p.sort()
en = 0
for i in range(0, K):
    en += p.pop(0)
print(en)
