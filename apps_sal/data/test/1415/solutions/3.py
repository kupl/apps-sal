x, y, x0, y0 = list(map(int, input().split()))
a = [[0] * (y + 1) for i in range(x + 1)]
s = input()
count = x * y
result = [0] * (len(s))
for i in range(len(s)):
    if a[x0][y0] == 0:
        a[x0][y0] = 1
        result[i] = 1
        count -= 1
    if s[i] == 'U' and x0 > 1:
        x0 -=1
    elif s[i] == 'D' and x0 < x:
        x0 +=1
    elif s[i] == 'L' and y0 > 1:
        y0 -= 1
    elif s[i] == 'R' and y0 < y:
        y0 += 1
        
print(" ".join(map(str,result)), count)

