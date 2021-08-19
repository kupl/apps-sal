n = int(input())
d = set()
data = list(map(int, input().split()))
ans = 0
for el in data:
    if el != 0:
        if not el in d:
            d.add(el)
            ans += 1
print(ans)
