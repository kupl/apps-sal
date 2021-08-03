import math
n = int(input())
w = list(map(int, input().split()))
x = 100
y = 200
tot = sum(w)
remain = (tot / 2) % 100
if n % 2 != 0 and ((x not in w) or (y not in w)):
    print("NO")
elif remain == 50:
    print("NO")
else:
    print("YES")
