I = [int(i) for i in input().split()]
n, c = I[0], I[1]
I = [int(i) for i in input().split()]
I_new = []
for i in range(1, n): I_new.append((I[i-1]-I[i]))
I_new.sort()
ans = I_new[-1]-c
if ans < 0: print(0)
else: print(ans)

