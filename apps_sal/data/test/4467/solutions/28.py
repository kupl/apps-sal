N = int(input())
Red = sorted([tuple(map(int, input().split())) for _ in range(N)])
Blue = sorted([tuple(map(int, input().split())) for _ in range(N)])

ans = 0
for bx, by in Blue:
    C = [(y, x) for x, y in Red if x < bx and y < by]  # 候補
    if len(C) == 0:
        continue
    ans += 1
    C.sort(reverse=True)
    Red.remove((C[0][1], C[0][0]))
print(ans)
