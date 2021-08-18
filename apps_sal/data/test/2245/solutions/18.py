from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    n, k = [int(x) for x in stdin.readline().split()]
    if k % 3 == 1:
        w = k + 2
    else:
        w = k + 1
    n_mod_w = n % w
    if n_mod_w % 3 in {1, 2} or n_mod_w == k:
        print('Alice')
    else:
        print('Bob')
