(n, w) = (int(i) for i in input().split())
tea = sorted((int(i) for i in input().split()))
smallest = min(tea[0], tea[n] / 2)
print(min(smallest * 3 * n, w))
