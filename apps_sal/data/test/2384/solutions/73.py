n = int(input())
A = list(map(int, input().split()))
if n % 2 == 0:
    ans1 = A[0]
    ans2 = A[1]
    for i in range((n - 2) // 2):
        ans2 = max(ans1, ans2) + A[(i + 1) * 2 + 1]
        ans1 = ans1 + +A[(i + 1) * 2]
    print(max([ans1, ans2]))

else:
    ans1, ans2, ans3, = A[0], A[1], A[2]
    for i in range((n - 2) // 2):
        ans3 = max(ans3, ans2) + A[(i + 2) * 2]
        ans2 = max(ans1, ans2) + A[(i + 2) * 2 - 1]
        ans1 = ans1 + A[(i + 1) * 2]
    print(max([ans1, ans2, ans3]))
