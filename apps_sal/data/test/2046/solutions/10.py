from sys import stdin as fin
# fin = open("cfr398a.in", "r")

n = int(fin.readline())
arr = list(map(int, fin.readline().split()))

pre = [False] * (n + 1)

maxab, l, r = n, 0, 0

for i in range(1, n + 1):
    pre[arr[i - 1]] = True
    if arr[i - 1] == maxab:
        while pre[maxab]:
            print(maxab, end=' ')
            pre[maxab] = False
            maxab -= 1
        print()
    else:
        print()
