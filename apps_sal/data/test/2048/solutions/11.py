def R(): return [int(i)for i in input().split()]


I = 3 * 10**8
n = int(input())
s, c = R(), R()
r = min(c[j] + min([I] + [c[i]for i in range(j)if
                          s[i] < s[j]]) + min([I] + [c[i] for i in range(j + 1, n)if
                                                     s[i] > s[j]])for j in range(n))
print((r, -1)[r > I])
