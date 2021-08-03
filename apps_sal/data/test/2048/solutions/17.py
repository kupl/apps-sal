def R(): return map(int, input().split())


I = 10**10
n = int(input())
s, c = list(R()), list(R())
r = min(c[j] + min([I] + [c[i]for i in range(j)if
                          s[i] < s[j]]) + min([I] + [c[i]for i in range(j + 1, n)if
                                                     s[i] > s[j]])for j in range(n))
print((r, -1)[r > I])
