from queue import Queue
s = input().strip()

neighbours = [[] for _ in range(10)]
for index_node in range(len(s)):
    value_node = int(s[index_node])
    neighbours[value_node].append(index_node)

distances = [-1] * len(s)
distances[0] = 0

q = Queue()
q.put(0)

while q.empty() == False:
    if distances[len(s) - 1] != -1:
        break
    current_node_index = q.get(0)
    value = int(s[current_node_index])
    for neighbour_index in neighbours[value]:
        if distances[neighbour_index] == -1:
            distances[neighbour_index] = distances[current_node_index] + 1
            q.put(neighbour_index)
    neighbours[value] = []
    if current_node_index + 1 < len(s) and distances[current_node_index + 1] == -1:
        distances[current_node_index + 1] = distances[current_node_index] + 1
        q.put(current_node_index + 1)
    if current_node_index - 1 > 0 and distances[current_node_index - 1] == -1:
        distances[current_node_index - 1] = distances[current_node_index] + 1
        q.put(current_node_index - 1)

print(distances[len(s) - 1])
