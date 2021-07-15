abc = list(map(int, input().split()))

print("Yes" if len(set(abc)) == 2 else "No")
