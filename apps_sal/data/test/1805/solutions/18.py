n = int(input())
for i in range(n):
    k = int(input())
    ans = max(4, k + k % 2)
    print(ans - k)
