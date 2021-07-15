def dd(i):
    return len(set(str(i))) == len(str(i))

L, R = list(map(int, input().split()))
for i in range(L, R+1):
    if dd(i):
        print(i)
        break
else:
    print(-1)


