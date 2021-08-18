N = int(input())


ans = N
while True:
    d = [int(i) for i in str(ans)]

    if sum(d) % 4 == 0:
        print(ans)
        break
    ans += 1
