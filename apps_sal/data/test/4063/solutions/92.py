N = int(input())
ary = list(map(int, input().split()))
ary.sort()

ans = ary[int(len(ary) / 2)] - ary[int(len(ary) / 2) - 1]
print(ans)
