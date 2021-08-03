def solve():
    n = int(input())
    a = [int(c) for c in input().split(" ")]
    total = sum(a)

    if n < 2:
        return None
    elif n == 2:
        if a[0] == a[1]:
            return None
        else:
            return (0,)
    else:
        for i in range(n):
            if a[i] != total - a[i]:
                return (i,)


result = solve()
if not result:
    print(-1)
else:
    print(len(result))
    for num in result:
        print(num + 1, end=" ")
