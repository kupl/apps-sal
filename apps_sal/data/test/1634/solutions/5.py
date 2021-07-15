c1,c2,c3 ,c4 = map(int,input().split())
n , m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ans1 = 0
ans2 = 0
for i in a:
    ans1 += min(c1 * i,c2)
ans1 = min(ans1, c3)
for i in b:
    ans2 += min(c1 * i,c2)
ans2 = min(ans2, c3)
ans = min(ans1 + ans2, c4)
print(ans)
