n = int(input())
l = list(map(int, input().split()))
pos = 0
neg = 0
w = []
for i in range(n):
    if l[i] >= 0:
        pos += 1
    else:
        neg += 1
    w.append(abs(l[i]))
if n == 1:
    print(l[0])
elif neg != 0 and pos == 0:
    print(sum(w) - min(w) * 2)
elif pos != 0 and neg == 0:
    print(sum(w) - min(w) * 2)
else:
    print(sum(w))
