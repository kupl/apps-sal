(A, B, C, D) = map(int, input().split())
area_ab = A * B
area_cd = C * D
if area_ab > area_cd:
    print(area_ab)
else:
    print(area_cd)
