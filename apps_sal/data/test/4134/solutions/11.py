n, m, k = list(map(int,input().split()))
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
# print(matrix)
d = [[{} for _ in range(m)] for _ in range(n)]
# print(d)
middle = (n + m - 2) // 2
# print(middle)
answer = 0

def upleft(x,y,acc,count):
    val = matrix[y][x]^acc
    if count == middle:
        if d[y][x].get(val) == None:
            d[y][x][val] = 1
            return
        else:
            d[y][x][val] += 1
            return
    else:
        if x + 1 < m:
            upleft(x+1,y,val,count+1)
        if y + 1 < n:
            upleft(x,y+1,val,count+1)

def downright(x,y,acc,count):
    nonlocal answer
    if count == n + m - 2 - middle:
        complement = k ^ acc
        if d[y][x].get(complement) != None:
            answer += d[y][x][complement]
        return
    else:
        val = matrix[y][x]^acc
        if x - 1 >= 0:
            downright(x-1,y,val,count+1)
        if y - 1 >= 0:
            downright(x,y-1,val,count+1)

upleft(0,0,0,0)
downright(m-1,n-1,0,0)
# print(d)
print(answer)

