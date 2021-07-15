AB, BC, CA = list(map(int, input().split()))
if (1 <= AB & AB <= 100) & (1 <= BC & BC <= 100) & (1 <= CA & CA <= 100):
    S = int(AB * BC / 2)
    print(S)

