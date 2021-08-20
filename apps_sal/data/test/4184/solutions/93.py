N = int(input())
W = list(map(int, input().split()))
diff = [0 for i in range(N - 1)]
for i in range(N - 1):
    S1 = sum(W[:i + 1])
    S2 = sum(W[i + 1:])
    diff[i] = abs(S1 - S2)
print(min(diff))
