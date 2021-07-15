cases = int(input())
for case in range(cases):
    L, v, l, r = [int(i) for i in input().split()]
    see_l = (l - 1)//v
    see_L = L//v
    see_r = r//v
    print(see_L+see_l-see_r)
