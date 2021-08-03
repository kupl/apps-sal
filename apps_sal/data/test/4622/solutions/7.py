n = int(input())
a = list(map(int, input().split()))
ans = len(a)
a1 = set(a)
ans1 = len(a1)

if ans == ans1:
    print("YES")
else:
    print("NO")
