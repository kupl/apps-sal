q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    s = input()
    m = 10**4
    for j in range(n):
        if j + k <= n:
            l1 = ["R", "G", "B"]
            m1, m2, m3 = 0, 0, 0
            for i in range(j, j + k):
                if l1[(i - j) % 3] != s[i]:
                    m1 += 1
            for i in range(j, j + k):
                if l1[(i + 1 - j) % 3] != s[i]:
                    m2 += 1
            for i in range(j, j + k):
                if l1[(i + 2 - j) % 3] != s[i]:
                    m3 += 1
            m = min(m, m1, m2, m3)
        else:
            break
    print(m)
