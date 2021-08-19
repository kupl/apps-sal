N = int(input())
(T, A) = map(float, input().split())
H = list(map(float, input().split()))
diff = [0 for i in range(N)]
for i in range(N):
    diff[i] = abs(A - (T - H[i] * 0.006))
print(diff.index(min(diff)) + 1)
