n, h = map(int, input().split())
print(sum(1 + (int(ai) > h) for ai in input().split()))
