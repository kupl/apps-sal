def LI():
    return list(map(int, input().split()))


(N, M) = LI()
x = M // N
for i in range(x, 0, -1):
    if M % i != 0:
        continue
    ans = i
    break
print(ans)
