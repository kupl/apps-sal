n = int(input())
ans = 0
ml = []
for i in range(n):
    a = int(input())
    ml.append(a)
x = max(ml) / 2
ans = sum(ml) - x
print(int(ans))
