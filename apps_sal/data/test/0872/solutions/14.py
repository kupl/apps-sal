n = int(input())
a = list(map(int, input().split()))
odd = sum((x % 2 == 1 for x in a))
if odd > 0 and odd < n:
    print(*sorted(a))
else:
    print(*a)
