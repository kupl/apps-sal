n = int(input())
s = list(map(int, input().split()))
M = max(s)
m = min(s)
i = M - m
s.remove(M)
M1 = max(s)
i1 = M1 - m
s.append(M)
s.remove(m)
m1 = min(s)
i2 = M - m1
print(min(i,i1,i2))

