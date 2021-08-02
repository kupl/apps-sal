N = input()
a = list(map(int, input().split()))

ans = []
for ai in a:
    ans.append(ai - 1)

print(sum(ans))
