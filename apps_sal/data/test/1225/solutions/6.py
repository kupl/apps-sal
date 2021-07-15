import math
H = int(input())
l = math.log(H,2)
ll = math.floor(l)+1
ans = 2 ** ll -1
print(ans)
