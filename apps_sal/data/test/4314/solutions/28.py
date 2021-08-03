h, w = list(map(int, input().split()))
A = [input() for _ in range(h)]
B = list()
ng = "." * w
cnt = 0
for i, a in enumerate(A):
    if a == ng:
        cnt += 1
    else:
        B.append(a)
A = list(["".join(x) for x in zip(*B)])
ng = "." * (h - cnt)
B = list()


for i, a in enumerate(A):
    if a == ng:
        cnt += 1
    else:
        B.append(a)

for a in zip(*B[::-1]):
    print(("".join(a[::-1])))
