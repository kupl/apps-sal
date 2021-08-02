n, k = map(int, input().split())
all = []
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    all += a
s = list(set(all))
print(n - len(s))
