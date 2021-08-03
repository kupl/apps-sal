[n, h, k] = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.insert(0, 0)
pref = [0]
for i in a:
    pref.append(pref[-1] + i)
free = [h] * (n + 1)
answer = [0] * (n + 1)
for i in range(1, n + 1):
    if a[i] <= free[i - 1]:
        answer[i] = answer[i - 1]
        free[i] = free[i - 1] - a[i]
    else:
        answer[i] = (a[i] - free[i - 1]) // k + 1
        if (a[i] - free[i - 1]) % k == 0:
            answer[i] -= 1
        free[i] = free[i - 1] + answer[i] * k
        if free[i] > h:
            free[i] = h
        free[i] -= a[i]
        answer[i] += answer[i - 1]
answer[n] += (h - free[n]) // k
if (h - free[n]) % k != 0:
    answer[n] += 1
print(answer[n])
