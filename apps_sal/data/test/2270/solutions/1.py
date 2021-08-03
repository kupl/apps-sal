n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [0] * (10 ** 5 + 5)
cnt4 = 0
cnt2 = 0
for i in range(n):
    b[a[i]] += 1
for elem in b:
    cnt4 += elem // 4
    cnt2 += elem // 2
for i in range(q):
    s = input().split()
    x = int(s[1])
    cnt4 -= b[x] // 4
    cnt2 -= b[x] // 2
    if s[0] == "+":
        b[x] += 1
    else:
        b[x] -= 1
    cnt4 += b[x] // 4
    cnt2 += b[x] // 2
    if cnt4 > 0:
        cnt = cnt2 - 2
        if cnt >= 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
