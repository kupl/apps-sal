N = int(input())
hum = [int(input()) for _ in range(5)]
print((N + min(hum) - 1) // min(hum) + 4)
