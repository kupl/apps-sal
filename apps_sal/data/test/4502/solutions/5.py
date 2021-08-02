n = int(input())
a = list(map(int, input().split()))
a1, a2 = [], []
for index, i in enumerate(a, start=1):
    if index % 2 == 0:
        a2.append(i)
    else:
        a1.append(i)

ans = []
if n % 2 == 0:
    ans = a2[::-1] + a1
else:
    ans = a1[::-1] + a2

print(" ".join(str(i) for i in ans))
