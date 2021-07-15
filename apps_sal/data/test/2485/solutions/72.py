import collections

h,w,m = map(int,input().split())
X = []
Y = []
for _ in range(m):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

most_common_x = collections.Counter(X).most_common()
most_common_x_index = most_common_x[0][0]
most_common_x_count = most_common_x[0][1]
most_common_y = collections.Counter(Y).most_common()
most_common_y_index = most_common_y[0][0]
most_common_y_count = most_common_y[0][1]

otherwisey = []
otherwisex = []
for i in range(m):
    if X[i] != most_common_x_index:
        otherwisey.append(Y[i])
    if Y[i] != most_common_y_index:
        otherwisex.append(X[i])

most_common_y = collections.Counter(otherwisey).most_common()
if len(most_common_y)!= 0:
    ansx = most_common_y[0][1] + most_common_x_count
else:
    ansx = most_common_x_count

most_common_x = collections.Counter(otherwisex).most_common()
if len(most_common_x)!= 0:
    ansy = most_common_x[0][1] + most_common_y_count
else:
    ansy = most_common_y_count

print(max(ansx,ansy))
