import fractions

N = int(input())
a = list(map(int, input().split()))

ans = sum(a) - N

print(ans)
