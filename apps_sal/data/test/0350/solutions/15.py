n = int(input())
l = list(map(int, input().split()))
l = sorted(l)[-1::-1]


for i in range(1, n):
    if l[i] >= l[i - 1]:
        l[i] = l[i - 1] - 1
    if l[i] < 0:
        l[i] = 0
print(sum(l))
