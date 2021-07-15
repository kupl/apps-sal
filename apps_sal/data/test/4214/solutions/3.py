xy=[[*map(int,input().split())] for _ in range(int(input()))]
print(sum(((i[0]-j[0])**2+(i[1]-j[1])**2)**.5 for j in xy for i in xy)/len(xy))
