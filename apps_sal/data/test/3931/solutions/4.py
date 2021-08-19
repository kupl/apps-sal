import heapq
import sys

num_trips, a, b, k, f = sys.stdin.readline().strip().split(" ")
a, b, k, f = int(a), int(b), int(k), int(f)
#print(a, b, k, f)
trips = []
for line in sys.stdin:
    trips.append(line.strip().split(" "))

"""
a = 5
b = 3
k = 1
f = 8

trips = [["BerBank", "University"],
["University", "BerMall"],
["University", "BerBank"],
["University", "BerBank"]]

"""

my_dict = dict()
for i in range(0, len(trips)):
    trip = trips[i]
    cost = 0
    if(i - 1 >= 0 and trips[i - 1][1] == trip[0]):
        cost = b
    else:
        cost = a
    if (str(sorted(trip)) in my_dict):
        my_dict[str(sorted(trip))] += cost
    else:
        my_dict[str(sorted(trip))] = cost

heap = [(-1 * my_dict[x], x) for x in my_dict]
heapq.heapify(heap)

# print(heap)
total = sum(int(my_dict[x]) for x in my_dict)
for i in range(0, k):
    if(len(heap) > 0):
        cur_max = int(heapq.heappop(heap)[0]) * -1
        if (cur_max > f):
            total = total - (cur_max - f)

print(total)
