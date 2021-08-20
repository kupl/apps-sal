(n, A, B) = [int(w) for w in input().split()]
s = [int(w) for w in input().split()]
S = sum(s)
(s1, *s) = s
s.sort()
s.reverse()
n = 0
while S * B > s1 * A:
    S -= s[n]
    n += 1
print(n)
