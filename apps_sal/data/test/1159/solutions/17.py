def ll():
    return list(map(int, input().split()))


testcases = 1
prime = []


def seive(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


for testcase in range(testcases):
    prime = seive(2005)
    [n] = ll()
    ii = n
    while prime[ii] != True:
        ii += 1
    ans = []
    for i in range(1, n):
        ans.append([i, i + 1])
    ans.append([n, 1])
    ii -= n
    if ii == 0:
        print(len(ans))
        for i in ans:
            print(*i)
        continue
    done = 1
    while ii != 0:
        ans.append([done, (done + 2) % (n + 1)])
        done += (done & 1 == 0) * 2
        done += 1
        ii -= 1
    print(len(ans))
    for i in ans:
        print(*i)
