3
gen = []
for i in range(1, 70):
    x = (1 << i) - 1
    for j in range(i - 1):
        gen.append(x ^ 1 << j)
gen = list(set(gen))
(a, b) = list(map(int, input().split()))
ans = 0
for y in gen:
    if a <= y <= b:
        ans += 1
print(ans)
