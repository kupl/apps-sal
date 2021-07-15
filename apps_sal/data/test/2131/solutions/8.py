import sys
import filecmp
import math
FILE_IO = False


CURR_PATH = []
list_of_connections = [[] for _ in range(100001)]

def dfs(vertex):
    visited, stack = set(), [vertex]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(list_of_connections[vertex]) - visited)
            if (len(set(list_of_connections[vertex]) - visited) == 0):
                CURR_PATH.append(vertex)




if FILE_IO:
    input_stream = open('input_test.txt')
    sys.stdout = open('current_output2.txt', 'w')
else:
    input_stream = sys.stdin

n = int(input_stream.readline())



for _ in range(n-1):
    input_list = input_stream.readline().split()
    start , end = int(input_list[0]),int(input_list[1])
    list_of_connections[start].append(end)
    list_of_connections[end].append(start)

max_edges = None
max_less_then_3 = None
no = False
for ind, edges in enumerate(list_of_connections):
    current_len = len(edges)
    if current_len > 2:
        if max_less_then_3 is not None:
            print('No')
            return
        else:
            max_less_then_3 = ind

if max_less_then_3 is None:
    max_less_then_3 = 1

print('Yes')
root = max_less_then_3

paths = []

visited = [False] * 100001
dfs(root) 

print(len(CURR_PATH))
for node in CURR_PATH:
    print(str(root) + " "+ str(node))
            


    

# if FILE_IO:
    # assert filecmp.cmp('current_output.txt','expected_output.txt',shallow=False) == True 

