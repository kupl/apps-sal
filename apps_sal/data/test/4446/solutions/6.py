(n, a, b, k) = map(int, input().split())
l1 = list(map(int, input().split()))
new = []
for x in l1:
    x = x % (a + b)
    if x > 0 and x <= a:
        new.append(0)
    else:
        if x == 0:
            x = a + b
        x -= a
        temp = x // a
        x = x - temp * a
        if x > 0:
            temp += 1
        new.append(temp)
new.sort()
answer = 0
for item in new:
    if k - item >= 0:
        k -= item
        answer += 1
    else:
        break
print(answer)
