n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
sm = sum(l1)
mx1 = max(l2)
l2.remove(mx1)
mx2 = max(l2)
if sm <= mx1 + mx2:
    print("YES")
else:
    print("NO")
