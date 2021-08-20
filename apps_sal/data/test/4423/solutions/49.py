n = int(input())
data = []
for i in range(n):
    (s, p) = input().split()
    tmp = [s, -int(p), i + 1]
    data.append(tmp)
data.sort()
for i in range(n):
    print(data[i][2])
