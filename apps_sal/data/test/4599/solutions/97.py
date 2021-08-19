def solve1(n, lst):
    alice, bob = 0, 0

    #print(" i |a[i]|Alice|Bob")
    # print("------------------")

    for i in range(n):
        if i % 2 == 0:
            alice += lst[i]
        else:
            bob += lst[i]
        # print(f"{i:3d}|{a[i]:3d}|{alice:5d}|{bob:5d}")

    return alice - bob


n = int(input())
a = list(map(int, input().split(" ")))
a.sort(reverse=True)
print((solve1(n, a)))
