X, Y = list(map(int, input().split()))
if X + Y < 2 or abs(X - Y) < 2: print("Brown")
else: print("Alice")
