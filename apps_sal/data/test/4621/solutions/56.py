h, w = map(int, input().split())
data = []
for i in range(h):
    data.append(input())
for i in range(2 * h):
    print(data[i // 2])
