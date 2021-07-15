from collections import Counter, defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ca = Counter(a)
cb = Counter(b)

for ka, va in list(ca.items()):
    vb = cb[ka]
    if va + vb > n:
        print("No")
        return

print("Yes")
end = defaultdict(int)
for i, e in enumerate(a):
    end[e] = i

mx = 0
for i, e in enumerate(b):
    diff = end[e] - i + 1
    mx = max(mx, diff)

ans = b[-mx:] + b[:-mx]
print((*ans))

