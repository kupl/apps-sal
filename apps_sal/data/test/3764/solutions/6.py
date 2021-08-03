inp = [
    (10, 10, 98), (1, 58, 62, 71, 55, 4, 20, 17, 25, 29)
]
def read(): return tuple(map(int, input().split()))


n, k, x = read()
l = sorted(read())
if k > 10:
    k = k % 4 + 4
for i in range(k):
    l = sorted([l[j] ^ x if j % 2 == 0 else l[j] for j in range(0, len(l), 1)])
print(max(l), min(l))
