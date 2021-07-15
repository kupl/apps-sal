n = int(input())
for i in range(n):
    lit, one, two = map(int, input().split())
    if two > one * 2:
        print(one * lit)
    else:
        print(two * (lit // 2) + one * (lit % 2))
