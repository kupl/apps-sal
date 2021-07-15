from itertools import combinations
cookies = tuple(map(int, input().split()))
if (S := sum(cookies)) & 1:
    print("No")
else:
    for r in range(4):
        for some_cookies in combinations(cookies, r):
            if sum(some_cookies) == S // 2:
                print("Yes")
                return
    print("No")
