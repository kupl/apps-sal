l, s, r, p = list(map(int, input().split()))
l2, s2, r2, p2 = list(map(int, input().split()))
l3, s3, r3, p3 = list(map(int, input().split()))
l4, s4, r4, p4 = list(map(int, input().split()))
if (l + s + r > 0 and p == 1) or (l2 + s2 + r2 > 0 and p2 == 1) or (l3 + s3 + r3 > 0 and p3 == 1) or (l4 + s4 + r4 > 0 and p4 == 1):
    print("YES")
else:
    if(l2 + s3 + r4 > 0 and p == 1) or (l3 + s4 + r > 0 and p2 == 1) or (l4 + s + r2 > 0 and p3 == 1) or (l + s2 + r3 > 0 and p4 == 1):
        print("YES")
    else:
        print("NO")
