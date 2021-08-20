n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    List = p[i:i + 3]
    P = List[1]
    num = sorted(List)[1]
    if P == num:
        ans += 1
print(ans)
