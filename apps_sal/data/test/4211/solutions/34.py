N = int(input())
li = list(map(int, input().split()))
rli = li[::-1]
rli.append(100001)
ans = [0] * N

ans[0] = rli[0]
for i in range(0, len(li)):
    ans[i + 1] = min(rli[i], rli[i + 1])

# print(ans)
print(sum(ans))
