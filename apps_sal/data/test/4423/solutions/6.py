N = int(input())

l = []

for i in range(N):
    s, p = input().split()

    l.append([i + 1, s, int(p)])

l = sorted(l, key=lambda x: x[2], reverse=True)
l = sorted(l, key=lambda x: x[1])

for x in l:
    print(x[0])
