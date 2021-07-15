n, q = map(int, input().split())
s = input()
lr = list(list(map(int, input().split()) for _ in range(q)))

c = [0]
for i in range(1, n):
    if s[i-1:i+1] == "AC":
        c.append(c[-1]+1)
    else:
        c.append(c[-1])

for l, r in lr:
    print(c[r-1] - c[l-1])
