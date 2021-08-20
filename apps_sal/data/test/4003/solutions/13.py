n = int(input())
M = list(map(int, input().split()))
L = [1] * n
R = [1] * n
for i in range(1, len(M)):
    if M[i] < M[i - 1]:
        R[i] = R[i - 1] + 1
    if M[n - 1 - i] < M[n - i]:
        L[n - 1 - i] = L[n - i] + 1
ans = []
last = -1
(l, r) = (0, n - 1)
while r >= l:
    if M[r] <= last and M[l] <= last:
        break
    if M[r] == M[l]:
        if L[l] > R[r]:
            ans += ['L']
            last = M[l]
            l += 1
        else:
            ans += ['R']
            last = M[r]
            r -= 1
    elif M[r] <= last:
        last = M[l]
        ans += ['L']
        l += 1
    elif M[l] <= last:
        last = M[r]
        ans += ['R']
        r -= 1
    elif M[l] < M[r]:
        last = M[l]
        ans += ['L']
        l += 1
    else:
        last = M[r]
        ans += ['R']
        r -= 1
print(len(ans))
print(''.join(ans))
