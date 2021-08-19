from queue import Queue
s = input().strip()

# contains a list of some the neibours indexes of a certain node (some are not     counted here : the one with index+1 and index-1)
neighbours = [[] for _ in range(10)]
for index_node in range(len(s)):
    value_node = int(s[index_node])
    neighbours[value_node].append(index_node)

# distance of every nodes to the source
distances = [-1] * len(s)
distances[0] = 0  # the distance of the source to itself with is 0

# This queue contains the index of the nodes we have not yet visited.
q = Queue()
q.put(0)  # initialize the q with the source node

while q.empty() == False:
    if distances[len(s) - 1] != -1:
        break
    # get() is same as the generic pop() operation
    current_node_index = q.get(0)
    value = int(s[current_node_index])
    # Relaxtion steps
    # check most of the neighbours
    for neighbour_index in neighbours[value]:
        # check if this neibhour was not visited before
        if distances[neighbour_index] == -1:
            distances[neighbour_index] = distances[current_node_index] + 1
            q.put(neighbour_index)
    neighbours[value] = []
    # check 2 others neighbours
    if current_node_index + 1 < len(s) and distances[current_node_index + 1] == -1:
        distances[current_node_index + 1] = distances[current_node_index] + 1
        q.put(current_node_index + 1)
    if current_node_index - 1 > 0 and distances[current_node_index - 1] == -1:
        distances[current_node_index - 1] = distances[current_node_index] + 1
        q.put(current_node_index - 1)

print(distances[len(s) - 1])
