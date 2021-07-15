D, G = list(map(int, input().split()))
p = [0] * D
c = [0] * D
for i in range(D):
    p[i], c[i] = list(map(int, input().split()))

ans = 1001
import math
for i in range(2**D):
    pp = 0
    t = 0
    b = format(i, "0" + str(D) + "b")
    #print(b)
    for j in range(D):
        pp += (100 * (j + 1) * p[j] + c[j]) * int(b[j])
        t += p[j] * int(b[j])
    if pp >= G:
        ans = min(ans, t)
        continue
    for k in range(D-1, -1, -1):
        if b[k] == "0":
            a = math.ceil((G - pp)//100/(k+1))
            if a < p[k]:
                t += a
                ans = min(ans, t)
                break
            else:
                t += p[k]-1
                pp += 100* (k + 1) *(p[k] - 1)

print(ans)

