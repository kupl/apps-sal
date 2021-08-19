(A, B, C, D) = map(int, input().split())
area1 = A * B
area2 = C * D
if area1 > area2 or area1 == area2:
    print(area1)
else:
    print(area2)
