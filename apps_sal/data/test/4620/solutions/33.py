n = int(input())
inp = []
for i in range(n-1):
    inp.append(list(map(int, input().split())))

for i in range(n-1):
    total = 0
    for j in range(i, n-1):
        if total < inp[j][1]:
            total = inp[j][1]
        while total % inp[j][2] != 0:
            total += 1
        total += inp[j][0]
    print(total)
print((0))
            




