N, K = map(int, input().split())

tem = N // K

print(min(abs(N - K * tem), abs(N - K * (tem + 1))))
