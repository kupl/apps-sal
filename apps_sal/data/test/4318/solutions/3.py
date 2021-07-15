N = int(input())
H = list(map(int,input().split()))

h = 1
yama = []
yama.append(H[0])

while h <= N - 1:
    if max(H[:h]) <= H[h]:
        yama.append(H[h])
    h += 1

print(len(yama))
