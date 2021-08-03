n = int(input())
# for i in range(t):
p = list(map(int, input().strip().split()))

l = [0] * n


for i in range(1, n + 1):
    l = [0] * (n + 1)
    j = i
    while(l[j] != 1):
        l[j] = l[j] + 1
        j = p[j - 1]
    print(j, end=" ")
