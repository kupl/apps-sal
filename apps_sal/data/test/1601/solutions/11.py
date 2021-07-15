def solve(points,ans,coords,x):
    arr = []
    curr = []
    y = points[0][0]
    for p in points:
        if p[0] == y:
            curr.append((y,p[1],p[2]))
        else:
            arr.append(curr)
            y = p[0]
            curr = [(y,p[1],p[2])]

    arr.append(curr)

    arr1 = []

    for i in arr:
        while len(i) >= 2:
            ans.append((i.pop(0)[2],i.pop(0)[2]))

        if len(i) == 1:
            arr1.append((i[0][0],i[0][1],i[0][2]))

    while len(arr1) >= 2:
        ans.append((arr1.pop(0)[2],arr1.pop(0)[2]))

    coords[x] = arr1[:]

def main():
    n = int(input())
    points = []
    coords = {}
    for i in range(n):
        x,y,z = list(map(int,input().split()))
        if x not in list(coords.keys()):
            coords[x] = [(y,z,i+1)]
        else:
            coords[x].append((y,z,i+1))

    ans = []

    for i in list(coords.keys()):
        coords[i].sort()
        if len(coords[i]) > 1:
            solve(coords[i],ans,coords,i)

        if len(coords[i]) == 1:
            points.append((i,coords[i][0][0],coords[i][0][1],coords[i][0][2]))

    points.sort()

    for i in range(0,len(points),2):
        a,b = points[i][3],points[i+1][3]
        ans.append((a,b))

    for i in ans:
        print(i[0],i[1])

main()

