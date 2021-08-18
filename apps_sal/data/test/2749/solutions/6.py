H, W = list(map(int, input().split()))
N = int(input())
a = list(map(int, input().split()))
s = []
for i in range(1, N + 1):
    for j in range(a[i - 1]):
        s.append(i)
num = 0
for i in range(H):
    tmp = []
    for j in range(W):
        tmp.append(s[num])
        num += 1

    if i % 2 == 1:
        tmp.reverse()
    print((*tmp))
