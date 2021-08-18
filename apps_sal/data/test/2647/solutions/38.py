h, w = list(map(int, input().split()))

matrix = [list('
count_sharp=0
for _ in range(h):
    C=list(input())
    count_sharp += C.count('
    matrix.append(['
matrix.append(list('

B=[[] for _ in range(10000)]


for i in range(h + 2):
    for j in range(w + 2):
        if matrix[i][j] == '.':
            if matrix[i - 1][j] == '.':
                B[100 * i + j].append(100 * (i - 1) + j)
            if matrix[i][j - 1] == '.':
                B[100 * i + j].append(100 * i + j - 1)
            if matrix[i][j + 1] == '.':
                B[100 * i + j].append(100 * i + j + 1)
            if matrix[i + 1][j] == '.':
                B[100 * i + j].append(100 * (i + 1) + j)



def solver(matrix, h, w, count_):
    path=[10000000] * 10000
    depth=0
    path[101]=0
    reached=[101]
    stack=[]
    stack.append(101)
    while len(stack) > 0:
        depth += 1
        for _ in range(len(stack)):
            val=stack.pop(0)
            for j in matrix[val]:
                if j not in set(reached):
                    path[j]=min(depth, path[j])
                    reached.append(j)
                    stack.append(j)

    if path[h * 100 + w] == 10000000:
        print((-1))
    else:
        print((h * w - path[h * 100 + w] - 1 - count_))


solver(B, h, w, count_sharp)
