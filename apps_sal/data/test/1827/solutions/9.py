n = int(input())
box = list(map(int, input().split()))
e = sum(box) // 2
box.sort()
for i in range(n):
    print(str(box[0]) + ' ' + str(box[-1]))
    box.pop(0)
    box.pop(-1)
