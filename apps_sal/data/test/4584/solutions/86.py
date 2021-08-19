N = int(input())
A = list(map(int, input().split()))
# A.reverse()
ans = [0 for _ in range(N)]
for i in reversed(range(N - 1)):
    # 今i番目(0index)の社員
    boss = A[i] - 1  # 0index
    ans[boss] += 1
    # print(ans,i,boss)
for x in ans:
    print(x)
