n_l = list(map(str, input().split()))

n_l.sort(reverse=True)

print((int(n_l[0] + n_l[1]) + int(n_l[-1])))

