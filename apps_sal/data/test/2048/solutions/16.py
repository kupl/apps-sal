def R(): return list(map(int, input().split()))


I = 2**29
n = int(input())
s, c = R(), R()
r = min(c[j] + min([c[i]for i in range(j)if
                    s[i] < s[j]], default=I) + min([c[i] for i in range(j + 1, n)if
                                                    s[i] > s[j]], default=I)for j in range(n))
print((r, -1)[r > I])
