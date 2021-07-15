n = int(input())
a = list(map(int, input().split()))

kind = len(set(a))

if (n-kind) % 2 == 0:
    ans = kind
else:
    ans =  kind - 1

print(ans)


