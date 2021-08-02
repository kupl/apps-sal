import math
A, B = input().split(' ')
if int(A) * float(B) >= 0:
    answer = math.floor(int(A) * float(B))
    print(answer)
else:
    answer = math.ceil(int(A) * float(B))
    print(answer)
