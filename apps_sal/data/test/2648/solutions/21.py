def abc053_d():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 0
    from collections import Counter
    multi_even = 0
    for (_, v) in Counter(A).items():
        ans += 1
        if 2 <= v and v % 2 == 0:
            multi_even += 1
    if 0 < multi_even and multi_even % 2 == 1:
        ans -= 1
    print(ans)


abc053_d()
