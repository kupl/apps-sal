w , h , n=map(int, input().split())
W = [1]*w
H = [1]*h

for i in range(n):
    x,y,a=map(int, input().split())
    if a == 1:
        for i in range(x):
            W[i] = 0
    if a == 2 :
        for i in range(x,w):
            W[i] = 0
    if a == 3:
        for i in range(y):
            H[i] = 0
    if a == 4:
        for i in range(y,h):
            H[i] = 0
print(sum(W)*sum(H))
