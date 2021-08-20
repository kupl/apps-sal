(n, m, k) = map(int, input().split())
p = list(map(int, input().split()))
rev = 1
new_rev = 1
page = None
count = 0
for i in range(m):
    if (p[i] - rev) // k != page:
        count += 1
        rev = new_rev
        page = (p[i] - rev) // k
    new_rev += 1
print(count)
