n = input()
t = list(map(int, input().split()))
n = [0 for _ in range(90)]
for i in t:
    n[i - 1] = 1
s = 0
ni = 0
for i in n:
    if ni == 15:
        break
    if i == 1:
        ni = 0
    elif i == 0:
        ni += 1
    s += 1
print(s)
