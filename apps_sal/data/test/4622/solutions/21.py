n = int(input())
a = list(map(int, input().split()))
an = set(a)

if len(a) == len(an):
    print("YES")
else:
    print("NO")
