d, t, s = map(int, input().split())
arrivalTime = d / s
print("Yes" if t >= arrivalTime else "No")
