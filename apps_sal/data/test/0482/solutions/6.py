(lambda n, k: print(*([chr(i + ord('a')) for i in range(k)] * (n // k + 1))[:n], sep=''))(*map(int, input().split()))
