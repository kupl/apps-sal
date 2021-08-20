n = int(input())
w = list(map(int, input().split()))
w2 = []
tmp = []
for i in range(n - 1):
    w2.append(w[0])
    w.pop(0)
    tmp.append(abs(sum(w) - sum(w2)))
print(min(tmp))
