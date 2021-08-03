a, s = map(int, input().split())
print("Impossible"if a % 3 and s % 3 and a % 3 == s % 3 else "Possible")
