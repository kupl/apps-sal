N, M = map(int, input().split())

print(pow(2, M) * (M * 1900 + (N - M) * 100))
