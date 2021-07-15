k, x = map(int, input().split())
print(' '.join(list(map(str, range(x-k+1, x+k)))))
