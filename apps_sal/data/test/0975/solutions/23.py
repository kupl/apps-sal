from collections import Counter
n = int(input())
s, m = [int(x) for x in input()], Counter([int(x) for x in input()])
m1 = Counter(m)
ans1, ans2 = 0, 0
for num1 in sorted([int(x) for x in s]):
    for num2 in range(num1+1, 10):
        if m[num2]:
            ans2 += 1
            m[num2] -= 1
            break
    else:
        break

for num1 in sorted(s):
    for num2 in range(num1, 10):
        if m1[num2]:
            ans1 += 1
            m1[num2] -= 1
            break
    else:
        break
print(n - ans1)
print(ans2)


