(k, x) = list(map(int, input().split()))
ans = [str(i) for i in range(x - k + 1, k + x)]
print(' '.join(ans))
