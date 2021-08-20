input()
print(sum((v - c for (v, c) in zip(map(int, input().split()), map(int, input().split())) if v - c > 0)))
