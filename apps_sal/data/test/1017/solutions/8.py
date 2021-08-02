def parse_int(): return list(map(int, input().split()))


n = int(input())

res = (n // 3) * 2
if n % 3 > 0:
    res += 1
print(res)
