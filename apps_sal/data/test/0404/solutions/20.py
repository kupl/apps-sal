a = int(input())
t = [0]
i = 2
while i * i <= a:
    if a % i == 0:
        t[len(t) - 1] += 1
        a = a / i
    else:
        i = i + 1
        if t[len(t) - 1] != 0:
            t.append(0)
if a > 1:
    if a != i:
        t.append(1)
    else:
        t[len(t) - 1] += 1
answer = 1
for i in t:
    answer *= i + 1
print(answer)
