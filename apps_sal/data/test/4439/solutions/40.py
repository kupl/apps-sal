A = int(input())
B = int(input())
lis = [1, 2, 3]
x = lis.index(A)
y = lis.index(B)
lis[x] = 0
lis[y] = 0
ans = sum(lis)
print(ans)
