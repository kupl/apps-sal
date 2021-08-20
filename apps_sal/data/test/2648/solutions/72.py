N = int(input())
A = [int(a) for a in input().split()]
z = {}
for n in A:
    if n in z:
        z[n] += 1
    else:
        z[n] = 1
cnt_even = 0
for (key, val) in list(z.items()):
    if val % 2 == 0:
        cnt_even += 1
cnt_odd = len(z) - cnt_even
tot = cnt_odd + cnt_even - cnt_even % 2
print(tot)
