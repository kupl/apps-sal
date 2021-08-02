def scanf(obj=list, type=int):
    return obj(list(map(type, input().split())))


n, = scanf()
m = scanf()
ans = [m[i - 1] for i in range(n) if i and m[i] == 1]
ans.append(m[-1])
print(len(ans))
print(*ans)
