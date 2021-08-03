a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = [input().split() for i in range(c)]
for i in range(c):
    print(sum(b) - b[int(d[i][0]) - 1] + int(d[i][1]))
