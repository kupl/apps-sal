h, l = list(map(int, input().split()))
ans = pow(l, 2) - pow(h, 2)
print(abs(ans / (2 * h)))
