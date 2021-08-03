N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
ans = [0, 0]
j = 0
now = -1
count = 1
for i in range(N):
    if A[i] == now:
        count += 1
        if count == 2:
            ans[j] = now
            if j == 1:
                print(ans[0] * ans[1])
                return
            j += 1
        if count == 4:
            print(now * now)
            return

    else:
        now = A[i]
        count = 1

print(0)
