n, k = map(int, input().split())
H = list(map(int, input().split()))
print(sum(h >= k for h in H))
