n = int(input())
a = list(map(int, input().split()))
s = sum(a)
x = [i ** 2 for i in a]
x = sum(x)
ans = (s ** 2 - x) // 2
print(ans % (10 ** 9 + 7))
