A, B, C = map(int, input().split())
ABC = sorted([A, B, C])
print(ABC[-1] * 10 + sum(ABC[:2]))
