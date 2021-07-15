n, w_max = list(map(int, input().split()))
W, V = [], []
Diff_zero = []
Diff_one = []
Diff_two = []
Diff_three = []
for i in range(n):
    w, v = list(map(int, input().split()))
    W.append(w)
    V.append(v)
    diff = w - W[0]
    if diff == 0:
        Diff_zero.append(v)
    elif diff == 1:
        Diff_one.append(v)
    elif diff == 2:
        Diff_two.append(v)
    elif diff == 3:
        Diff_three.append(v)

Diff_zero = sorted(Diff_zero, reverse=True)
Diff_one = sorted(Diff_one, reverse=True)
Diff_two = sorted(Diff_two, reverse=True)
Diff_three = sorted(Diff_three, reverse=True)

Diff_zero_ruiseki = [0]
Diff_one_ruiseki = [0]
Diff_two_ruiseki = [0]
Diff_three_ruiseki = [0]

for i in range(len(Diff_zero)):
    Diff_zero_ruiseki.append(Diff_zero[i] + Diff_zero_ruiseki[-1])
for i in range(len(Diff_one)):
    Diff_one_ruiseki.append(Diff_one[i] + Diff_one_ruiseki[-1])
for i in range(len(Diff_two)):
    Diff_two_ruiseki.append(Diff_two[i] + Diff_two_ruiseki[-1])
for i in range(len(Diff_three)):
    Diff_three_ruiseki.append(Diff_three[i] + Diff_three_ruiseki[-1])

value_max = 0
w_zero = W[0]

for i in range(n+1):
    if i > len(Diff_zero):
        continue
    for j in range(n+1):
        if j > len(Diff_one):
            continue
        for k in range(n+1):
            if k > len(Diff_two):
                continue
            for l in range(n+1):
                if l > len(Diff_three):
                    continue
                if w_zero*i + (w_zero+1)*j + (w_zero+2)*k + (w_zero+3)*l > w_max:
                    continue
                if i + j + k + l > n:
                    continue

                value = Diff_zero_ruiseki[i] + Diff_one_ruiseki[j] + Diff_two_ruiseki[k] + Diff_three_ruiseki[l]
                value_max = max(value, value_max)

print(value_max)


             

