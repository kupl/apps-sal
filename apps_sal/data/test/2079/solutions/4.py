n = int(input())


w = list(map(int, input().split()))


s = input()

for i in range(n):
    w[i] = [w[i], i]
w.sort(reverse=True)
exos = []
locs = [-1 for i in range(2 * n)]
for i in range(2 * n):
    if(s[i] == '0'):
        exos.append(w.pop())
        locs[i] = exos[-1][1] + 1
    else:
        temp = exos.pop()
        locs[i] = temp[1] + 1
print(*locs)
