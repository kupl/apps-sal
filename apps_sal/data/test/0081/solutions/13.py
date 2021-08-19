(a, b) = list(map(int, input().split()))
(a, b) = (min(a, b), max(a, b))
gap = b - a
arr = []
i = 1
while i * i < gap:
    if gap % i == 0:
        arr.append(i)
        arr.append(gap // i)
    i += 1
if i * i == gap:
    arr.append(i)
arr.sort()
answer = 0
value = 10 ** 20
for i in arr:
    plus = 0
    if a % i:
        plus = i - a % i
    (ta, tb) = (a + plus, b + plus)
    mod = ta % tb
    while mod:
        ta = tb
        tb = mod
        mod = ta % tb
    temp = (a + plus) * (b + plus) // tb
    if temp < value:
        value = temp
        answer = plus
    if temp == value:
        answer = min(answer, plus)
print(answer)
