import queue
n = int(input())
dic = {}

for i in range(n + 1):
    dic[i] = []
for i in range(n - 1):
    u, v = [int(x) for x in input().split()]
    dic[u].append(v)
    dic[v].append(u)

weight = {1: (0, 1)}  # No.City:(length,weight)
q = queue.Queue()
q.put(1)
while(q.empty() == False):
    city = q.get()
    choice = len(dic[city])
    if city > 1:
        choice = choice - 1
    for to_city in dic[city]:
        if to_city not in weight:
            weight[to_city] = (weight[city][0] + 1, weight[city][1] / choice)
            q.put(to_city)
    if(choice > 0):
        weight[city] = (weight[city][0], 0)

sum = 0
for city in weight:
    sum = sum + weight[city][0] * weight[city][1]

print("%.15f" % sum)
