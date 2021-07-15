n, k = input().split()
n, k = int(n), int(k)

cisel_vlavo = n * (k-1)
prve_v_k = cisel_vlavo + 1
prve_vlavo = 1

riadok_vpravo = n - k + 1
cislo = prve_v_k
su = 0
for _ in range(n):
    su += cislo
    cislo += riadok_vpravo
print(su)

for r in range(n):
    space = False
    for c in range(1, n+1):
        if space:
            print(" ", end="")
        else:
            space = True
        if c < k:
            print(prve_vlavo, end="")
            prve_vlavo += 1
        else:
            print(prve_v_k, end="")
            prve_v_k += 1
        
    print()
