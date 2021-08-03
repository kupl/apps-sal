for _ in range(int(input())):
    dest, v, l, r = map(int, input().split())
    tot = dest // v
    upto_l = (l - 1) // v
    upto_r = r // v
    print(tot - (upto_r - upto_l))
