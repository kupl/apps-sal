r1, c1, r2, c2 = map(int, input().split())

p = 10 ** 9 + 7
size = 1010000 * 2
f_list = [1] * size
for i in range(1, size):
    f_list[i] = (f_list[i - 1] * i) % p

def cmb(n, r):
    return f_list[n + r] * pow(f_list[n], p-2, p) * pow(f_list[r], p-2, p) % p

hole = cmb(r2 + 1, c2 + 1) - 1
rect1 = cmb(r2 + 1, c1) - 1
rect2 = cmb(r1, c2 + 1) - 1
duplicate = cmb(r1, c1) - 1
ans = (hole - rect1 - rect2 + duplicate) % p
print(ans)
