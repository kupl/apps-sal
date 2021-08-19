N = int(input())
ans = (10 ** N - 9 ** N - 9 ** N + 8 ** N) % int(1000000000.0 + 7)
print(int(ans))
