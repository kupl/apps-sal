(s, t) = ([], [])
for i in range(int(input())):
    s.append(input())
for i in range(int(input())):
    t.append(input())
profit = 0
for i in s:
    temp = s.count(i) - t.count(i)
    if profit < temp:
        profit = temp
print(profit)
