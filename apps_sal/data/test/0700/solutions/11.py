N = int(input())
map_1 = [list(input()) for i in range(N)]
map_2 = [list(input()) for i in range(N)]
maps = list()
maps.append([[map_2[i][j] for j in range(N)] for i in range(N)])
maps.append([[map_2[i][N - 1 - j] for j in range(N)] for i in range(N)])
maps.append([[map_2[N - 1 - i][j] for j in range(N)] for i in range(N)])
maps.append([[map_2[N - 1 - i][N - 1 - j] for j in range(N)] for i in range(N)])
maps.append([[map_2[j][i] for j in range(N)] for i in range(N)])
maps.append([[map_2[j][N - 1 - i] for j in range(N)] for i in range(N)])
maps.append([[map_2[N - 1 - j][i] for j in range(N)] for i in range(N)])
maps.append([[map_2[N - 1 - j][N - 1 - i] for j in range(N)] for i in range(N)])
print(('No', 'Yes')[any((map_1 == el for el in maps))])
