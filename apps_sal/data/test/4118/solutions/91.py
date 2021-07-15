a, b = map(int,input().split())
print(a*b if a < 10 and b < 10 and a > 0 and b > 0 else -1)
