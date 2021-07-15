n = int(input())
h = list(map(int, input().split()))

s = 0

for i in range(max(h)+1):
    flag = False
    for j in range(n):
        if flag and h[j] == 0:
            s += 1
            flag = False
        elif not flag and h[j] > 0:
            flag = True

        h[j] = max(h[j]-1, 0)
    if flag:
        s += 1

print(s)


