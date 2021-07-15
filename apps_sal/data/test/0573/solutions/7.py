n = int(input())
a = [int(i) for i in input().split()]
ans = min(a.count(2), a.count(1)) + (a.count(1) - min(a.count(2), a.count(1))) // 3
print(ans)
