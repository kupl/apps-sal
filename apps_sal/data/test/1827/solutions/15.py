n = int(input())
l = sorted(list(map(int, input().split(' '))))
length = l[0] + l[-1]
for i in range(n):
    print(l[i], length - l[i])
