S = input()
K = int(input())
one = 0

for s in S:
    if s == "1":
        one += 1
    else:
        ans = s
        break

if K <= one:
    print(1)
else:
    print(ans)
