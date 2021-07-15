
class Node: 
    def __init__(self, id):
        self.id = id
        self.parent = -1
        self.children = set()
        self.apples = 1

nodes = dict()

nb_nodes = int(input())
for i in range(nb_nodes): 
    nodes[i+1] = Node(i+1)

parents = [int(i) for i in input().split(" ")]

base = 2
for p in parents: 
    nodes[base].parent = p
    nodes[p].children.add(base)
    base += 1

#for n in nodes.values(): 
#    print("%d -> %s" % (n.id, n.children))
    
recolt = 0
todo = { 1 }
while len(todo) > 0: 
    recolt += len(todo) % 2
    next = set()
    for t in todo: 
        next |= nodes[t].children
    todo = next
        
print(recolt)
