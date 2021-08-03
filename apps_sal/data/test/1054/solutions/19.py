a = int(input(""))
XlistOfCoordinates = []
YlistOfCoordinates = []
for value in range(a):
    y = input("").split(" ")
    XlistOfCoordinates.append(int(y[0]))
    YlistOfCoordinates.append(int(y[1]))
print(max(max(XlistOfCoordinates) - min(XlistOfCoordinates), max(YlistOfCoordinates) - min(YlistOfCoordinates))**2)
