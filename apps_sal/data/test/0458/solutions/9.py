import math
a, b, c = map(int, input().split())
ans = []
for i in range(1, 82):
    x = b * (i ** a) + c
    if i == sum(list(map(int, str(abs(x))))) and x < 10 ** 9 and x > 0:
        ans.append(x)
print(len(ans))
if (len(ans)):
    print(*ans)
