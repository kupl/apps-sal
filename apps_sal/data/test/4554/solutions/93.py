W, A, B = map(int, input().split())
print(max(abs(B - A) - W, 0))
