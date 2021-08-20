(N, K) = map(int, input().split())
D = list(map(int, input().split()))
s = set(D)
for i in range(N, 10 ** 6 + 1):
    l = [j for j in str(i)]
    flag = True
    for n in l:
        if int(n) in s:
            flag = False
            break
    if flag:
        ans = i
        break
print(ans)
