n = int(input())
l = list(map(int, input().split()))
l.sort()
ans1 = l[-2] - l[0]
ans2 = l[-1] - l[1]
print(min(ans1, ans2))
