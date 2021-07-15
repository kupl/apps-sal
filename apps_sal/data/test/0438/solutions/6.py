n = int(input()) - 1
ans = [1]
while n > ans[-1]:
    n -= ans[-1] + 1
    ans.append(ans[-1] + 1)
ans[-1] += n
print(len(ans))
print(*ans)
