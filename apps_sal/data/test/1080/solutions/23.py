n = int(input())
assert(2 <= n <= 100000)

li = list(map(int, input().split()))
su = sum(li)
if su % 2 == 0:
    for item in li:
        if su < item << 1:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")
