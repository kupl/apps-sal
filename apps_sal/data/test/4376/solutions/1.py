n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
minus = 0
id = 0
for i in b:
    while 1:
        if i - minus > a[id]:
            minus += a[id]
            id += 1
        else:
            print(id + 1, i - minus)
            break
