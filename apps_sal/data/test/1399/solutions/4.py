from math import gcd
n = int(input())
pts = []
ans = 0
for i in range(0, n):
    a, b, A, B = tuple(map(int, input().split(' ')))
    pts.append((a, b, A, B))
    ans += (gcd(abs(a - A), abs(b - B)) + 1)
m = dict()
for i in range(n):
    for j in range(i + 1, n):
        a1 = pts[i][0]
        b1 = pts[i][1]
        a2 = pts[i][2]
        b2 = pts[i][3]
        A1 = pts[j][0]
        B1 = pts[j][1]
        A2 = pts[j][2]
        B2 = pts[j][3]
        num1 = (b2 - B2) * (A2 - A1) * (a2 - a1) + A2 * (a2 - a1) * (B2 - B1) - a2 * (A2 - A1) * (b2 - b1)
        den1 = (B2 - B1) * (a2 - a1) - (b2 - b1) * (A2 - A1)
        if(den1 != 0 and num1 % den1 == 0):
            if(a1 == a2):
                num2 = B2 * (A2 - A1) + (num1 // den1 - A2) * (B2 - B1)
                den2 = (A2 - A1)
                if(num2 % den2 == 0):
                    if((num1 // den1 - A2) * (num1 // den1 - A1) <= 0 and (num2 // den2 - B2) * (num2 // den2 - B1) <= 0 and (num1 // den1 - a2) * (num1 // den1 - a1) <= 0 and (num2 // den2 - b2) * (num2 // den2 - b1) <= 0):
                        if((num1 // den1, num2 // den2) not in m):
                            m[(num1 // den1, num2 // den2)] = set()
                        m[(num1 // den1, num2 // den2)].add(i)
                        m[(num1 // den1, num2 // den2)].add(j)
            else:
                num2 = b2 * (a2 - a1) + (num1 // den1 - a2) * (b2 - b1)
                den2 = (a2 - a1)
                if(num2 % den2 == 0):
                    if((num1 // den1 - A2) * (num1 // den1 - A1) <= 0 and (num2 // den2 - B2) * (num2 // den2 - B1) <= 0 and (num1 // den1 - a2) * (num1 // den1 - a1) <= 0 and (num2 // den2 - b2) * (num2 // den2 - b1) <= 0):
                        if((num1 // den1, num2 // den2) not in m):
                            m[(num1 // den1, num2 // den2)] = set()
                        m[(num1 // den1, num2 // den2)].add(i)
                        m[(num1 // den1, num2 // den2)].add(j)
sum = 0
for i in list(m.values()):
    sum += (len(i) - 1)
print(ans - sum)
