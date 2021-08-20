(n, x) = list(map(int, input().split()))
sample_gram = 0
l1 = []
for i in range(0, n):
    m = int(input())
    sample_gram += m
    l1.append(m)
if sample_gram > x:
    noofdonut = sample_gram // x
    print(int(noofdonut))
elif sample_gram == x:
    print(int(sample_gram / m))
elif sample_gram < x:
    initial_donut = n
    reamaning_gram = x - sample_gram
    l = []
    for j in range(0, n):
        a = reamaning_gram / l1[j]
        l.append(int(a))
    print(initial_donut + int(max(l)))
