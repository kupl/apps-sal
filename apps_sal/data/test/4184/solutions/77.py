N = int(input())
W = map(int, input().split())
weigt_list = list(W)
T = 1
ans = []
for i in range(N - 1):
    S1 = sum(weigt_list[0:T])
    S2 = sum(weigt_list[T:])
    difference = abs(S1 - S2)
    ans.append(difference)
    T += 1
print(min(ans))
