def ll():
    return list(map(int, input().split()))


n = int(input())
l = ll()
ans = 2 + (l[2] ^ min(l))
print(ans)
