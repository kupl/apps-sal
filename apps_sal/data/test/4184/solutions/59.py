N = int(input())
W = list(map(int, input().split()))
difference_list = []
for T in range(N - 1):
    S1 = sum(W[:T + 1])
    S2 = sum(W[T + 1:])
    difference_list.append(abs(S1 - S2))
    ans = min(difference_list)
print(ans)
