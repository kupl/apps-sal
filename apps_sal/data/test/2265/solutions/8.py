a = [int(x) for x in list(input())]
b = [int(x) for x in list(input())]
n = len(b)
counter = odd = answer = 0
for i in range(n):
    if a[i] != b[i]:
        counter += 1
    if i != n - 1 and a[i] != a[i + 1]:
        odd += 1
if counter % 2 == 0:
    flag = True
    answer += 1
else:
    flag = False
odd %= 2
for i in range(n, len(a)):
    if a[i] != a[i - 1]:
        odd += 1
        odd = odd % 2
    if odd == 0:
        if flag:
            answer += 1
    else:
        if flag:
            flag = False
        else:
            answer += 1
            flag = True
    if a[i - n] != a[i - n + 1]:
        odd += 1
        odd %= 2
print(answer)
