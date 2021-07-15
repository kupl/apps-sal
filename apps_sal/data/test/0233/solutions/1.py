n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
m = sum([a[i][0] > a[i][1] for i in range(n)])
c = sum([a[i][0] < a[i][1] for i in range(n)])
if m > c: print("Mishka")
elif m == c: print("Friendship is magic!^^")
else: print("Chris")
