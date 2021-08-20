(l1, s1, r1, p1) = list(map(int, input().split()))
(l2, s2, r2, p2) = list(map(int, input().split()))
(l3, s3, r3, p3) = list(map(int, input().split()))
(l4, s4, r4, p4) = list(map(int, input().split()))
if p1 and (r1 or s1 or l1 or r4 or l2 or s3) or (p2 and (r2 or s2 or l2 or l3 or r1 or s4)) or (p3 and (r3 or s3 or l3 or l4 or r2 or s1)) or (p4 and (r4 or s4 or l4 or l1 or r3 or s2)):
    print('YES')
else:
    print('NO')
