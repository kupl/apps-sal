n, m = map(int, input().split())
tom = list(map(int, input().split()))
ban = list(map(int, input().split()))
a1 = max(tom)
a2 = min(tom)
b1 = max(ban)
b2 = min(ban)
if max(a1 * b1, a1 * b2) <= max(a2 * b1, a2 * b2):
    tom.remove(a2)
else:
    tom.remove(a1)
r = -0x3f3f3f3f3f3f3f3f
for i in tom:
    for j in ban:
        if i * j > r:
            r = i * j
print(r, flush=True)
