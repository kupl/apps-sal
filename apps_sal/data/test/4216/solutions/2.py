import math
n = int(input())
ans = 10
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        ans2 = max(len(str(i)), len(str(n // i)))
        #print(i,len(str(i)), len(str(n//i)))
        if ans > ans2:
            ans = ans2
print(ans)
