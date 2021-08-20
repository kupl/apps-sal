(N, K) = map(int, input().split())
H = list(map(int, input().split()))
ANS = sum((x >= K for x in H))
print(ANS)
