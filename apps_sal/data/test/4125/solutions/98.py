def make_divisors(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


a = [int(s) for s in input().split()]
N = a[0]
st = a[1]
mini = int(-1)
b = [int(s) for s in input().split()]
for i in range(N):
    if abs(b[i] - st) < mini or mini == -1:
        mini = abs(b[i] - st)
yakulist = make_divisors(mini)
gyakulist = sorted(yakulist, reverse=True)
kazu = len(gyakulist)
flag = int(0)
for i in range(kazu):
    for j in range(N):
        if abs(b[j] - st) % gyakulist[i] != 0:
            flag = 1
        else:
            pass
    if flag == 0:
        print(gyakulist[i])
        break
    else:
        flag = 0
