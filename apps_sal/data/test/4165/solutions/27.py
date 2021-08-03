n = int(input())
long = list(map(int, input().split()))
one = max(long)
ans = sum(long) - one

if ans > one:
    print("Yes")
else:
    print("No")
