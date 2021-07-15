from operator import xor

def dfs(d, start, finish):
    visited = []
    temp = []
    while True:
        if start not in visited:
            visited.append(start)
            [temp.append(item) for item in d[start]]
        if not temp:
            return False
        temp.reverse()
        start = temp.pop()
        temp.reverse()
        if start == finish:
            return True

n = int(input())
dict = {}
list = []
for i in range(n):
    line = [int(item) for item in input().split()]
    if line[0] == 1:
        dict[(line[1], line[2])] = set()
        list.append((line[1], line[2]))
        for (a, b) in dict:
            if xor(line[1] < a and a < line[2], line[1] < b and b < line[2]):
                dict[(line[1], line[2])].add((a,b))
                dict[(a,b)].add((line[1], line[2]))
            if a > line[1] and b < line[2]:
                dict[(a,b)].add((line[1], line[2]))
    else:
        first = list[line[1]-1]
        finish = list[line[2]-1]
        if dfs(dict, first, finish):
            print('YES')
        else:
            print('NO')
