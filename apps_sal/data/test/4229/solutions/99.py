N = int(input())

cnt = 0
for i in range(N+1):
    if i % 15 == 0:
        pass
    elif i % 3 == 0:
        pass
    elif i % 5 == 0:
        pass
    else:
        cnt += i

print(cnt)

