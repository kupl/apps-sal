n = int(input())
slv = dict()
arr = []
matrix = [[0] * n for i in range(n)]
for i in range(n):
    curr = input()
    if slv.get(curr) == None:
        slv[curr] = 1
    else:
        slv[curr] += 1
print(max(slv.values()))
