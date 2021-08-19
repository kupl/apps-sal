n = int(input())
t, a = list(map(int, input().split()))
points = list(map(int, input().split()))
# print(points)

mypoints = []
for i in range(len(points)):
    mypoints.append(t - points[i] * 0.006)
# print(mypoints)

subpoints = []
for j in range(len(points)):
    subpoints.append(abs(a - mypoints[j]))

# print(subpoints)
# print(min(subpoints))
print((subpoints.index(min(subpoints)) + 1))
