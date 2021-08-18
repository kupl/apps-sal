
input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

candi = []
for x in a:
    mx = x * b[0]
    for y in b:
        mx = max(mx, x * y)

    candi.append(mx)

candi.sort()
print(candi[-2])
