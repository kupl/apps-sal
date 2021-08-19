number, length = input().split()
number, length = int(number), int(length)

distances = [int(n) for n in input().split()]
distances = sorted(distances)
ans = 0
for i in range(1, len(distances)):
    ans = max(ans, distances[i] - distances[i - 1])

# print(ans/float(2))
if max(ans / float(2), min(distances) - 0, length - max(distances)) == ans / float(2):
    #print(ans/float(2), min(distances)- 0, length- max(distances))
    print(ans / float(2))
else:
    print(max(min(distances) - 0, length - max(distances)))
