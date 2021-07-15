N = int(input())
X_list = list(map(int, input().split()))
tmp = X_list.copy()

tmp.sort()
a = tmp[int(N/2)-1]
b = tmp[int(N/2)]
for i in range(N):
    if(X_list[i] <= a):
        print(b)
    else:
        print(a)
