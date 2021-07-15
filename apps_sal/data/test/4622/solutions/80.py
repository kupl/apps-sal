n = int(input())

a = list(map(int, input().split()))


x = len(set(a))


if x == len(a):
    print("YES")
else:
    print("NO")
