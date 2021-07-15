n = int(input())

xy = []
for index in range(n):
  x, y = map(int, input().split())
  xy.append([x, y])

pos_max = xy[0][0]+xy[0][1]
pos_min = xy[0][0]+xy[0][1]
neg_max = xy[0][0]-xy[0][1]
neg_min = xy[0][0]-xy[0][1]
for item in xy:
  pos_v = item[0] + item[1]
  neg_v = item[0] - item[1]
  pos_max = pos_v if pos_v > pos_max else pos_max
  pos_min = pos_v if pos_v < pos_min else pos_min
  neg_max = neg_v if neg_v > neg_max else neg_max
  neg_min = neg_v if neg_v < neg_min else neg_min

pos_result = pos_max - pos_min
neg_result = neg_max - neg_min
print(pos_result if pos_result >= neg_result else neg_result)
