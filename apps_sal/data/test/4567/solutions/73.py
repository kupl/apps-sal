N = int(input())
dp = [0]
for i in range(N):
    P = int(input())
    dp_p = list(map(lambda x: x + P, dp))
    dp = list(set(dp + dp_p))

P_List = [0] + [i for i in dp if i % 10 != 0]
print(max(P_List))
