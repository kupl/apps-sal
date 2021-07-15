n, d = list(map(int, input().split()))
a = input()
m = list(map(len, a.split("1")))
pos = 1
out = 0

if max(m) >= d:
    print(-1)
    return

else:
    while pos != n:
        for i in range(d, 0, -1):
            if pos + i > n:
                pass

            else:
                if a[pos + i - 1] == "1":
                    pos += i
                    out += 1
                    break

print(out)
