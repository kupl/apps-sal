N = int(input())
points = []
for i in range(0, N):
    points.append(list(map(int, input().split(' '))))
X = dict()
Y = dict()
count = 0
for p in points:
    if p[0] not in X.keys():
        X[p[0]] = []
    X[p[0]].append(p[1])
    if p[1] not in Y.keys():
        Y[p[1]] = []
    Y[p[1]].append(p[0])
while len(X.items()) > 0:
    item = list(X.items())[0]
    del X[item[0]]
    queue = [item]
    point_dict = {'x': [], 'y': []}
    queue_is_x = [True]
    while len(queue) > 0:
        item = queue.pop(0)
        is_x = queue_is_x.pop(0)
        if is_x:
            point_dict['x'].append(item[0])
            for i in item[1]:
                if i in Y.keys():
                    queue.append((i, Y[i]))
                    queue_is_x.append(False)
                    del Y[i]
        else:
            point_dict['y'].append(item[0])
            for i in item[1]:
                if i in X.keys():
                    queue.append((i, X[i]))
                    queue_is_x.append(True)
                    del X[i]
    # print((point_dict['x']))
    # print(len((point_dict['x'])))
    # print((point_dict['y']))
    # print(len((point_dict['y'])))
    count += len(set(point_dict['x'])) * len(set(point_dict['y']))

print(count - len(points))
