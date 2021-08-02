n, c = list(map(int, input().split()))
p1 = list(map(int, input().split()))
p2 = p1[::-1]
t = list(map(int, input().split()))
t1 = [t[0]]
for x in t[1:]: t1 += [t1[-1] + x]
t2 = [t[-1]]
for x in t[:-1][::-1]: t2 += [t2[-1] + x]
s1 = s2 = 0
for i in range(n):
    s1 += max(0, p1[i] - c * t1[i])
    s2 += max(0, p2[i] - c * t2[i])
if s1 == s2: print("Tie")
if s1 > s2: print("Limak")
if s1 < s2: print("Radewoosh")
