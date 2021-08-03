n = int(input())

num = [int(input()) for _ in range(n)]
num.sort()

begin = 0
end = n - 1
ans = 0

while begin <= end:
    if begin == end:
        ans += (num[begin] * num[end])
        ans %= 10007
    else:
        ans += 2 * num[begin] * num[end]
        ans %= 10007
    begin += 1
    end -= 1

print(ans)
