(H, N) = map(int, input().split())
Skills = list(map(int, input().split()))
Total = sum(Skills)
if H <= Total:
    print('Yes')
else:
    print('No')
