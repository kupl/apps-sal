import math
R = lambda: list(map(int, input().split()))
n, a, b = R()
k = math.ceil(math.log(n, 2))
i = 1
while (a != b):
    a = (a + 1) // 2
    b = (b + 1) // 2
    i += 1

res = i - 1
if res == k:
    print("Final!")
else:
    print(res)
