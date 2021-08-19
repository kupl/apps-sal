#fin = open("input.txt")
n = int(input())
#n = int(fin.readline())
X1, Y1, X2, Y2 = 10 ** 9 * 2, 10 ** 9 * 2, -10 ** 9 * 2, -10 ** 9 * 2
for i in range(n):
    x, y = list(map(int, input().split()))
    #x, y = map(int, fin.readline().split())
    X1, Y1, X2, Y2 = min(X1, x), min(Y1, y), max(X2, x), max(Y2, y)
print(max((X2 - X1), (Y2 - Y1)) ** 2)
