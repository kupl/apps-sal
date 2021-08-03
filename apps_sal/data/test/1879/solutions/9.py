N, sx, sy, dx, dy = tuple(int(i) for i in input().split())
A = input()
answered = False
for i in range(len(A)):
    if(A[i] == "N" and sy < dy):
        sy += 1
    elif(A[i] == "S" and sy > dy):
        sy -= 1
    elif(A[i] == "E" and sx < dx):
        sx += 1
    elif(A[i] == "W" and sx > dx):
        sx -= 1

    if(sx == dx and sy == dy):
        print(i + 1)
        answered = True
        break

if(not answered):
    print("-1")
