n = int(input())
OBE = [list(map(int, input().split())) for i in range(n)]
CL = [list(map(int, input().split())) for i in range(n)]

OBE.sort(key=lambda x: x[1])
OBE.sort(key=lambda x: x[0])
CL.sort(key=lambda x: x[1])
CL.sort(key=lambda x: x[0])

print(OBE[0][0] + CL[-1][0], OBE[0][1] + CL[-1][1])
