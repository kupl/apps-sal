s = input()
n = int(input())
d = 1
left = ""
right = ""

for i in range(n):
    q = input()

    if q == "1":
        d *= -1

    else:
        _, f, c = q.split()

        if d == 1:
            if f == "1":
                left += c

            else:
                right += c

        else:
            if f == "2":
                left += c

            else:
                right += c

ans = left[::-1] + s + right

print(ans[::d])
