N, H = map(int, input().split())
l = []
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

B.sort(reverse=True)
ans = 0
n = max(A)
flag = True
for i in range(N):
    if B[i] > n:
        ans += 1
        H -= B[i]
        if H <= 0:
            flag = False
            break
    else:
        break
if flag:
    ans += H // n
    if H % n != 0:
        ans += 1
print(ans)
