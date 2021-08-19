import bisect
n = int(input())


def primelist(N):
    prime = [2]
    for i in range(3, N + 1):
        flag = 1
        for j in prime:
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            prime.append(i)
    return prime


prime = primelist(n + 100)
ans = []
for i in range(n - 1):
    ans.append([i + 1, i + 2])
ans.append([1, n])
index = bisect.bisect_left(prime, n)
more = prime[index] - n
mid = n // 2
for i in range(1, more + 1):
    ans.append([i, mid + i])
print(len(ans))
for i in range(len(ans)):
    print(' '.join(map(str, ans[i])))
