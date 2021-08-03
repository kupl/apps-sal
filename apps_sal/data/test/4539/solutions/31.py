N = int(input())
n = sum(map(int, str(N)))
print("Yes" if N % n == 0 else "No")
